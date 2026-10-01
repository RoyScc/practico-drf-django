from django.contrib import admin
from .models import Paciente, Receta

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Receta)