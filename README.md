# Documentación de API REST con Flask e integración externa

## Descripción general

Este proyecto implementa una API REST desarrollada en Python utilizando Flask. La aplicación permite gestionar un conjunto de recursos mediante operaciones CRUD almacenadas en memoria. 

Adicionalmente, se integra un servicio externo de consulta de datos a través de API Ninjas, permitiendo obtener información de animales mediante solicitudes HTTP.

El objetivo del proyecto es practicar la creación de endpoints, manejo de peticiones HTTP y consumo de APIs externas.

---

## Requisitos del sistema

- Python
- pip (gestor de paquetes de Python)
- Flask
- requests
- python-dotenv
- Herramienta para pruebas de API (Postman o similar)

---

## Instalación y configuración

### Instalación de dependencias

pip install flask requests python-dotenv

---

### Variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

API_KEY=2RReAZCGt6ARy9RmZY13Quxbj5k4gEtByoBUsHRe

---

### Ejecución del servidor

python main.py

Servidor disponible en:

http://127.0.0.1:5000

---

## Endpoints

### Obtener todos los recursos
GET /api/recursos

### Obtener recurso por ID
GET /api/recursos/<id>

### Crear recurso
POST /api/recursos

Body:
{
  "nombre": "ejemplo"
}

### Actualizar recurso
PUT /api/recursos/<id>

Body:
{
  "nombre": "actualizado"
}

### Eliminar recurso
DELETE /api/recursos/<id>

---

## Notas

- Los datos del CRUD se almacenan en memoria.
- La API externa requiere una API Key válida.
- El servidor debe reiniciarse tras cambios en el código.