from django.contrib import admin
from .models import Paciente, Receta

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'apellido', 'nombre', 'dni', 'obra_social', 'fecha_registro')
    
    search_fields = ('apellido', 'nombre', 'dni')
    
    list_filter = ('obra_social',)
    
    ordering = ('apellido',)

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'medicamento', 'dosis', 'fecha_emision')
    
    search_fields = ('medicamento', 'paciente__apellido')
    
    list_filter = ('fecha_emision',)