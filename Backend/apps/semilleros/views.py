
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from apps.semilleros.serializers import SemilleroSerializer
from apps.semilleros.models import Semillero

# Create your views here.

class SemillerolistAV(APIView):

    def get(self, request):
        semilleros = Semillero.objects.all()
        serializer = SemilleroSerializer(semilleros, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SemilleroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
