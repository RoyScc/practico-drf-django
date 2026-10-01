from django.urls import path
from . import views

from .views import ListaPacientes

urlpatterns = [
    path('pacientes/', views.ListaPacientes.as_view(), name='lista-pacientes'),
    path('pacientes/<int:id>/', views.detalle_paciente, name='detalle-paciente'),
    path('pacientes/', ListaPacientes.as_view(), name='lista-pacientes'),
    # path('pacientes/<int:id>/', DetallePaciente.as_view(), name='detalle-paciente'),
]