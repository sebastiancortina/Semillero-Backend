
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from api.serializers import SemilleroSerializer
from apps.semilleros.models import Semillero

# Create your views here.

class SemillerolistAV(APIView):
    
    # Listar semilleros
    def get(self, request):
        semilleros = Semillero.objects.filter(activo=True)
        serializer = SemilleroSerializer(semilleros, many=True)
        return Response(serializer.data)
    
    
    #Crear semillero
    def post(self, request):
        serializer = SemilleroSerializer(data=request.data)
        
        #serializer = SemilleroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data['usuarios'], status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Listar semilleros aprobados
class SemillerolistAprobado(APIView):
        def get(self, request):
            semilleros = Semillero.objects.filter(aprobado=True)
            serializer = SemilleroSerializer(semilleros, many=True)
            return Response(serializer.data)

class SemilleroDetalleAV(APIView):
    def get(self, request, id):
        try: 
            semilleros = Semillero.objects.get(id=id)
            serializer = SemilleroSerializer(semilleros)
            return Response(serializer.data)

        except Semillero.DoesNotExist:
            return Response({'error': 'Semillero no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try: 
            semilleros = Semillero.objects.get(id=id)
            serializer = SemilleroSerializer(semilleros, data= request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Semillero.DoesNotExist:
            return Response({'error': 'Semillero no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):

        try: 
            semilleros = Semillero.objects.get(id=id)
            semilleros.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Semillero.DoesNotExist:
            return Response({'error': 'Semillero no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
