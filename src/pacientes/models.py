from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    obra_social = models.CharField(max_length=100, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - DNI: {self.dni}"

class Receta(models.Model):
    # conecta la receta con un paciente existente
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='recetas')
    medicamento = models.CharField(max_length=200)
    dosis = models.CharField(max_length=100)
    indicaciones = models.TextField(blank=True, null=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receta de {self.medicamento} para {self.paciente.apellido}"