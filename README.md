# API Gestión de Tareas / Notas Inteligentes

Proyecto backend desarrollado con **Django** y **Django REST Framework (DRF)** para crear una API de gestión de notas.

El proyecto permite registrar usuarios, iniciar sesión mediante JWT y realizar operaciones CRUD sobre las notas de cada usuario.

## Tecnologías utilizadas

* Python
* Django
* Django REST Framework
* Simple JWT
* SQLite

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar en la carpeta:

```bash
cd api_notas
```

Crear el entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual en Windows:

```bash
..\venv\Scripts\Activate.ps1
..\venv\Scripts\activate.bat
python manage.py runserver
```

Instalar las dependencias:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

## Configuración de la base de datos

Ejecutar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Crear usuario administrador

Para crear un usuario administrador:

```bash
python manage.py createsuperuser
```

## Ejecutar el proyecto

Iniciar el servidor:

```bash
python manage.py runserver
```

La API estará disponible en:

```text
http://127.0.0.1:8000/
```

## Endpoints principales

### Registro

Permite crear un nuevo usuario.

```text
POST /api/register/
```

Ejemplo:

```json
{
    "username": "juan",
    "password": "12345678",
    "email": "juan@gmail.com"
}
```

### Login

Permite obtener los tokens JWT.

```text
POST /api/token/
```

Ejemplo:

```json
{
    "username": "juan",
    "password": "12345678"
}
```

### Renovar token

```text
POST /api/token/refresh/
```

Ejemplo:

```json
{
    "refresh": "TU_REFRESH_TOKEN"
}
```

## Notas

Todas las operaciones de notas requieren autenticación mediante JWT.

Para las peticiones protegidas se debe enviar:

```text
Authorization: Bearer TU_ACCESS_TOKEN
```

### Listar notas

```text
GET /api/notas/
```

### Crear nota

```text
POST /api/notas/
```

Ejemplo:

```json
{
    "titulo": "Mi primera nota",
    "contenido": "Contenido de mi nota"
}
```

### Ver una nota

```text
GET /api/notas/1/
```

### Modificar una nota

```text
PUT /api/notas/1/
```

Ejemplo:

```json
{
    "titulo": "Nota modificada",
    "contenido": "Contenido nuevo"
}
```

### Eliminar una nota

```text
DELETE /api/notas/1/
```

## Búsqueda

Se pueden buscar notas por título o contenido.

```text
GET /api/notas/?buscar=django
```

## Estadísticas

Permite consultar la cantidad de notas del usuario autenticado.

```text
GET /api/notas/estadisticas/
```

Ejemplo de respuesta:

```json
{
    "total_notas": 5
}
```

## Paginación

Las notas están paginadas a **5 elementos por página**.

Primera página:

```text
GET /api/notas/
```

Segunda página:

```text
GET /api/notas/?page=2
```

También se puede combinar con la búsqueda:

```text
GET /api/notas/?buscar=django&page=2
```

## Seguridad

Cada usuario solamente puede acceder a sus propias notas.

Las notas de otros usuarios no son visibles aunque estén registradas en la misma base de datos.

La autenticación se realiza mediante tokens JWT.

## Estructura del proyecto

```text
api_notas/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── notas/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── admin.py
│
├── venv/
├── db.sqlite3
├── manage.py
└── README.md
```

## Autor

Proyecto realizado como práctica académica utilizando Django y Django REST Framework.
