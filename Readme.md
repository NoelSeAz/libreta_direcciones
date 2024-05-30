# Libreta de Direcciones

Esta aplicación permite gestionar una libreta de direcciones utilizando técnicas de Programación Orientada a Objetos (OOP) en Python. También se integra el uso de pandas para la manipulación de datos y SQLite para la persistencia de los mismos.

## Funcionalidades

- Buscar contacto
- Añadir contacto
- Modificar contacto
- Eliminar contacto

## Requisitos

- Python 3.x
- Pandas
- SQLite3

## Instalación

### Paso 1: Clonar el Repositorio

Clona este repositorio en tu máquina local.
- git clone https://github.com/tu_usuario/libreta_direcciones.git
- cd libreta_direcciones

### Paso 2: Crear el Entorno Virtual

Crea y activa un entorno virtual.python -m venv venv
- source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

### Paso 3: Instalar Dependencias

Instala las dependencias necesarias.
- pip install pandas

## Uso

Ejecutar la Aplicación
Para ejecutar la aplicación, ejecuta el script interfaz.py.
python interfaz.py

## Archivos Principales

- contacto.py
Define la clase Contacto, que representa a un individuo en la libreta de direcciones.

- libreta_direcciones.py
Maneja una colección de objetos Contacto y proporciona métodos para buscar, añadir, modificar y eliminar contactos.

- interfaz.py
Proporciona una interfaz de texto para interactuar con la libreta de direcciones.

## Contribuir

Si deseas contribuir a este proyecto, por favor, crea un fork del repositorio, realiza tus cambios y envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.