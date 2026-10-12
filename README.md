# 🏥 API REST - Centro Médico (Gestión de Pacientes y Recetas)

Trabajo práctico evaluativo desarrollado con **Django** y **Django REST Framework (DRF)**. El sistema implementa una API REST para administrar pacientes y sus recetas médicas asociadas mediante serializadores anidados, ViewSets y Autenticación JWT.

---

## 🚀 Características y Evolución

### Tercer Práctico (Octubre)
* **ViewSets y Routers:** Reemplazo de vistas manuales por `ModelViewSet` (Pacientes) y `ReadOnlyModelViewSet` (Recetas) con enrutamiento automático mediante `DefaultRouter`.
* **Autenticación JWT:** Seguridad en los endpoints implementada con `restframework-simplejwt`. Requiere token Bearer para acceder y modificar los datos.
* **Throttling (Límite de Peticiones):** Configuración nativa en DRF para limitar las solicitudes a 10 por minuto por usuario (`UserRateThrottle`) previniendo abusos a la API.
* **Panel de Administración Personalizado:** Modelos registrados en el panel de Django usando `ModelAdmin` con filtros, barras de búsqueda y visualización en columnas ordenadas.

### Segundo Práctico (01/10) 
* **Modelos Relacionados:** Relación uno a muchos (1:N) entre `Paciente` y `Receta` implementada con `ForeignKey`.
* **Serializadores Anidados:** Inclusión automática de las recetas médicas asociadas dentro de la consulta detallada de cada paciente mediante `read_only=True`.
* **Vistas Basadas en Clases:** Implementación de operaciones CRUD completas utilizando `APIView` (`get`, `post`, `put`, `delete`).
* **Manejo de Respuestas HTTP:** Códigos de estado semánticos (`200 OK`, `201 Created`, `204 No Content`, `400 Bad Request` y `404 Not Found`).

---

## 🛠️ Tecnologías

* **Lenguaje:** Python 3.12
* **Framework:** Django
* **Toolkit:** Django REST Framework
* **Seguridad:** Simple JWT
* **Base de Datos:** SQLite3
* **Gestor de Entorno y Paquetes:** `uv`
* **Cliente REST para Pruebas:** Insomnia

---

## ⚙️ Instalación y Ejecución en Linux

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/RoyScc/e-recetas.git](https://github.com/RoyScc/e-recetas.git)
   cd e-recetas