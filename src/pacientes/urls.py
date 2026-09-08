from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.lista_pacientes, name='lista-pacientes'),
    path('pacientes/<int:id>/', views.detalle_paciente, name='detalle-paciente'),
]