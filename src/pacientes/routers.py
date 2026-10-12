# from nucleo.urls import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import PacienteViewSet, RecetaViewSet


# enruto los viewsets de la API
router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet, basename='pacientes')    # API de pacientes
router.register(r'recetas', RecetaViewSet, basename='recetas')           # API de recetas

urlpatterns = router.urls