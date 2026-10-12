
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from .views import ListaPacientes


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('pacientes.routers')),

    # endpoints para la autenticación
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # ahora el ser asi se puede ver los pacientes : [http://127.0.0.1:8000/api/pacientes/]
    # path('', include("pacientes.urls"))
]
