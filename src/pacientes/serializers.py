from rest_framework import serializers
from .models import Paciente

# Serializer:
# "Traductor" del ORM hacia un body JSON de la api y viceversa
# También se encarga de validar datos, y dar acceso a otras utilidades del orm como el .save()

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'  #trae todos los datos de la BD y cconvierte a JSON

# serializer anidado para las Recetas de un Paciente
class RecetasSerializer(serializers.ModelSerializer):
    recetas = PacienteSerializer(read_only=True) # se pasa el serializer anidado de la receta

    class Meta:
        model = Paciente
        fields = '__all__'

    read_only_fields = ('paciente','id')
