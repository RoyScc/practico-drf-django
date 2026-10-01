# 🏥 API REST - Centro Médico (Gestión de Pacientes y Recetas)

Trabajo práctico evaluativo desarrollado con **Django** y **Django REST Framework (DRF)**. El sistema implementa una API REST para administrar pacientes y sus recetas médicas asociadas mediante serializadores anidados y Vistas Basadas en Clases (`APIView`).

---

## 🚀 Características hasta el momento (01/10 - Segundo practico) 

* **Modelos Relacionados:** Relación uno a muchos (1:N) entre `Paciente` y `Receta` implementada con `ForeignKey`.
* **Serializadores Anidados:** Inclusión automática de las recetas médicas asociadas dentro de la consulta detallada de cada paciente mediante `read_only=True`.
* **Vistas Basadas en Clases:** Implementación de operaciones CRUD completas utilizando `APIView` (`get`, `post`, `put`, `delete`).
* **Manejo de Respuestas HTTP:** Códigos de estado semánticos (`200 OK`, `201 Created`, `204 No Content`, `400 Bad Request` y `404 Not Found`).

---

## 🛠️ Tecnologías

* **Lenguaje:** Python 3.12
* **Framework:** Django
* **Toolkit:** Django REST Framework
* **Base de Datos:** SQLite3
* **Gestor de Entorno y Paquetes:** `uv`
* **Cliente REST para Pruebas:** Insomnia

---

## ⚙️ Instalación y Ejecución en Linux

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/RoyScc/e-recetas.git](https://github.com/RoyScc/e-recetas.git)
   cd e-recetas

2. **Acceder al directorio del proyecto e instalar dependencias:**
cd src
uv sync

3. **Ejecutar migraciones de la base de datos:**
uv run manage.py makemigrations
uv run manage.py migrate

4. **Iniciar el servidor local:**
uv run manage.py runserver

5. **FIN**
### El servicio quedará disponible en: http://127.0.0.1:8000/
