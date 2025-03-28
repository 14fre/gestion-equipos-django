# Gestión de Equipos con Django

Este es un proyecto desarrollado en Django 4.2 para la gestión de equipos tecnológicos. Permite a los usuarios registrarse, iniciar sesión y administrar equipos, incluyendo funciones para registrar, editar, eliminar y reportar daños. Está conectado a una base de datos MySQL usando XAMPP.

## Características
- **Autenticación**: Registro de usuarios y login para acceder al sistema.
- **Gestión de Equipos**: 
  - Registrar nuevos equipos con nombre, tipo, descripción y ubicación.
  - Editar información de equipos existentes.
  - Eliminar equipos.
  - Reportar daños y dar de baja equipos.
- **Interfaz**: Plantillas HTML con estilos CSS embebidos para una experiencia sencilla y funcional.
- **Base de Datos**: Usa MySQL (configurado con XAMPP) para almacenar equipos, reportes y usuarios.

## Requisitos
- Python 3.x (probado con 3.13.2)
- Django 4.2
- XAMPP (con MySQL/MariaDB 10.4 o superior)
- Git (para clonar el repositorio)

## Instalación
Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/14fre/gestion-equipos-django.git
   cd gestion-equipos-django
