import cv2  # Gestión de imágenes
import mediapipe as mp  # Reconocimiento facial
import os  # Gestión de archivos y carpetas
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import requests
from PIL import Image, ImageTk  # Para manejar la imagen de fondo

# Configuración inicial
nombre = "Franklyn"
ruta = os.path.join("C:/Users/Frank/PycharmProjects/Rostro_Api/.venv/Fotos")
carpeta = os.path.join(ruta, nombre)

if not os.path.exists(carpeta):
    os.makedirs(carpeta)

contador = 0

# Función para capturar y guardar imágenes de rostro
def capturar_rostro():
    global contador
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Error", "No se pudo acceder a la cámara")
        return

    detector = mp.solutions.face_detection
    with detector.FaceDetection(min_detection_confidence=0.75) as rostros:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)  # Corrección de efecto espejo
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            resultado = rostros.process(rgb)

            if resultado.detections is not None:
                for rostro in resultado.detections:
                    al, an, _ = frame.shape
                    xi = int(rostro.location_data.relative_bounding_box.xmin * an)
                    yi = int(rostro.location_data.relative_bounding_box.ymin * al)
                    ancho = int(rostro.location_data.relative_bounding_box.width * an)
                    alto = int(rostro.location_data.relative_bounding_box.height * al)

                    xf, yf = xi + ancho, yi + alto
                    cara = frame[yi:yf, xi:xf]
                    cara = cv2.resize(cara, (150, 200), interpolation=cv2.INTER_CUBIC)

                    # Guardar la imagen del rostro
                    cv2.imwrite(os.path.join(carpeta, f"rostro_{contador}.jpg"), cara)
                    contador += 1

            cv2.imshow("Reconocimiento facial", frame)
            tecla = cv2.waitKey(1)
            if tecla == 27 or contador >= 5:  # Limita la captura a 5 imágenes
                break

    cap.release()
    cv2.destroyAllWindows()

# Función para registrar entrada
def registrar_entrada():
    capturar_rostro()
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    payload = {"accion": "entrada", "hora": hora}
    enviar_datos(payload)
    messagebox.showinfo("Registro", f"Entrada registrada a las {hora}")

# Función para registrar salida
def registrar_salida():
    capturar_rostro()
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    payload = {"accion": "salida", "hora": hora}
    enviar_datos(payload)
    messagebox.showinfo("Registro", f"Salida registrada a las {hora}")

# Función para enviar datos a la API REST
def enviar_datos(payload):
    try:
        url = "TinedoSenati2024.somee.com/cambiarEstadoRostro1"
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Datos enviados correctamente:", response.json())
        else:
            print("Error al enviar datos:", response.status_code, response.text)
    except Exception as e:
        print("Error al conectar con la API:", e)

# Crear ventana de botones con Tkinter
root = tk.Tk()
root.title("Control de Asistencia")
root.geometry("526x789")  # Tamaño de la ventana

# Cargar imagen de fondo
ruta_imagen = "C:/Users/Frank/OneDrive/Imágenes/Fondos/yuki.jpg"
if os.path.exists(ruta_imagen):
    background_image = Image.open(ruta_imagen)
    background_image = background_image.resize((526, 789), Image.Resampling.LANCZOS)  # Cambiado por LANCZOS
    background_photo = ImageTk.PhotoImage(background_image)
else:
    messagebox.showerror("Error", "La imagen de fondo no se encontró.")
    root.destroy()  # Salir si no hay imagen de fondo

# Crear Canvas y añadir imagen de fondo
canvas = tk.Canvas(root, width=526, height=789)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Añadir botones al Canvas
btn_entrada = tk.Button(root, text="Registrar Entrada", command=registrar_entrada, width=20, bg="green", fg="white")
btn_salida = tk.Button(root, text="Registrar Salida", command=registrar_salida, width=20, bg="red", fg="white")

canvas.create_window(263, 500, window=btn_entrada)  # Centrar botón
canvas.create_window(263, 550, window=btn_salida)  # Centrar botón

root.mainloop()
