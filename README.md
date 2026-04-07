# Face Recognition API - Control de Asistencia Biométrico

![Versión](https://img.shields.io/badge/Versi%C3%B3n-1.0.0-orange)
![Tecnologías](https://img.shields.io/badge/Stack-Node.js%20%7C%20Flutter%20%7C%20MySQL-green)

Esta API proporciona una solución inteligente para el control de asistencia laboral mediante el reconocimiento de rostros en tiempo real. Está diseñada para integrarse con aplicaciones móviles o terminales de quiosco, permitiendo un registro de entradas y salidas seguro, rápido y sin contacto.

## 🚀 Funcionalidades

- **Reconocimiento Facial 1:N:** Identificación de trabajadores comparando el rostro detectado contra una base de datos de empleados.
- **Registro de Asistencia:** Marcación automática de ingreso y salida con marcas de tiempo (timestamps) precisas.
- **Detección de Liveness (Anti-Suplantación):** Algoritmos para prevenir el uso de fotografías o videos para engañar al sistema.
- **Gestión de Usuarios:** API endpoints para el registro (enrolamiento) de nuevos rostros y gestión de datos del personal.
- **Panel Administrativo:** Consulta de reportes de asistencia y métricas de puntualidad.

## 🛠️ Stack Tecnológico

- **Backend:** Node.js con Express
- **Frontend:** Flutter (Mobile App)
- **Base de Datos:** MySQL
- **Procesamiento de Imágenes:** Algoritmos de Biometría Facial

## 📂 Estructura del Repositorio

- `/api`: Servidor central y lógica de autenticación.
- `/models`: Definición de esquemas de datos y entrenamiento facial.
- `/controllers`: Manejo de peticiones de reconocimiento y registro.
- `/database`: Scripts de creación y migración de tablas en MySQL.

## 🔧 Configuración Rápida

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/FranklynRT/Api_rostro_reconocimiento.git](https://github.com/FranklynRT/Api_rostro_reconocimiento.git)
