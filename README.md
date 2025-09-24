# CRM Python Mongo  

Proyecto para aplicar conocimientos en MongoDB y Python, creando un CRM (Customer Relationship Management) básico que permita gestionar clientes y sus interacciones.

## Descripción del Proyecto

Estara desarrollado en FastAPI y MongoDB, permitiendo realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los clientes y sus interacciones.

## Tecnologías Utilizadas

- Python
- FastAPI
- MongoDB
- Beanie (ODM para MongoDB)
- Pydantic (para validación de datos)
- Uvicorn (servidor ASGI)


## Ejecutar de forma local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/mrGoonies/mini_crm.git
    cd mini_crm
    ```
2. Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. Asegúrate de tener MongoDB corriendo en tu máquina local o usa un servicio de MongoDB en la nube.
4. Configura las variables de entorno necesarias (por ejemplo, la cadena de conexión a MongoDB).
5. Ejecuta la aplicación:
    ```bash
    uvicorn main:app --reload
    ```
6. Abre tu navegador y ve a `http://localhost:8000/docs` para ver la documentación de la API generada automáticamente por FastAPI.

