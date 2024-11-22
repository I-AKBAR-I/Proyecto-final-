# Proyecto final 
# Realizado Por :
Kevin Andres Cubides
Jose David Velasco
# Sistema de Cotización de Ventanas

Este proyecto es un sistema de cotización de ventanas desarrollado con **Python** y **Flask**, diseñado para calcular costos basados en dimensiones, materiales y estilos. Además, permite aplicar descuentos y generar resúmenes en formato PDF.

## Arquitectura del Proyecto

El sistema sigue una arquitectura basada en contenedores, que incluye:

1. **Proxy (Nginx):** Maneja las solicitudes y las redirige al frontend o a la API.
2. **Frontend (Flask):** Proporciona la interfaz gráfica para los usuarios.
3. **API:** Gestiona la lógica del negocio y se comunica con la base de datos.
4. **Base de Datos (PostgreSQL):** Almacena información relacionada con los pedidos, clientes y configuraciones.

## Características Principales

- Manejo de estilos de ventanas y selección de materiales.
- Cálculo de costos basado en dimensiones y materiales.
- Gestión de descuentos para pedidos grandes.
- Generación de resúmenes detallados en PDF.
- Almacenamiento de datos en base de datos PostgreSQL.
- Escalabilidad y mantenibilidad del sistema.

## Requisitos Previos

Asegúrate de tener instalados los siguientes programas:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.10+ (si deseas probar localmente)

## Instalación

### 1. Clona este repositorio:

```bash
git clone https://github.com/I-AKBAR-I/Proyecto_Cotizacion.git
cd Proyecto_Cotizacion
