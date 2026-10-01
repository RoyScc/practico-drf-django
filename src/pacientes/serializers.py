from rest_framework import serializers
from .models import Paciente

# Serializer:
# "Traductor" del ORM hacia un body JSON de la api y viceversa
# También se encarga de validar datos, y dar acceso a otras utilidades del orm como el .save()

class PacienteSerializer(serializers.ModelSerializer):
    recetas = RecetaSerializer(many=True, read_only=True)

    class Meta:
        model = Paciente
        fields = '__all__'

    

# serializer anidado para las Recetas de un Paciente
class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta 
        fields = '__all__'  #trae todos los datos de la BD y cconvierte a JSON