from django.shortcuts import render, get_object_or_404
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PacienteSerializer
from .models import Paciente

# clase para pacientes API → extensiones de views

class ListaPacientes(APIView):
    def get(self, request):
        pacientes = Paciente.objects.all()
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(
                {"mensaje": "Paciente creado"}, status=status.HTTP_201_CREATED
            )
        return Response(
            {"mensaje": "No se creó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# crud usando cualquiera de las API Views basadas en clases concretas de views
def detalle_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id) 
    serializer = PacienteSerializer(paciente)
    return Response(serializer.data)

    if request.method == 'GET':    
        serializer = PacienteSerializer(paciente)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PacienteSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        paciente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def lista_pacientes(request):
#     if request.method == 'GET':
#         pacientes = Paciente.objects.all()
#         serializer = PacienteSerializer(pacientes, many=True)
#         return Response(serializer.data)
        
#     if request.method == 'POST':
#         serializer = PacienteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save() 
#             return Response(
#                 {"mensaje": "Paciente creado"}, status=status.HTTP_201_CREATED
#             )
#         return Response(
#             {"mensaje": "No se creó porque no es válido"},
#             status=status.HTTP_400_BAD_REQUEST,
#         )
            


# @api_view(['GET', 'PUT', 'DELETE'])
# def detalle_paciente(request, id):
#     paciente = get_object_or_404(Paciente, id=id) 

#     if request.method == 'GET':
#         serializer = PacienteSerializer(paciente)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PacienteSerializer(paciente, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         paciente.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)