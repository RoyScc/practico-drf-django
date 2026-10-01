from django.urls import path
from . import views




# from .views import ListaPacientes

urlpatterns = [
    path('pacientes/', views.ListaPacientes.as_view(), name='lista-pacientes'),
    path('pacientes/', views.DetallePaciente.as_view(), name='detalle-pacientes'),
    path('pacientes/<int:id>/', views.DetallePaciente.as_view(), name='detalle-paciente'),
    # path('pacientes/<int:id>/', DetallePaciente.as_view(), name='detalle-paciente'),
]