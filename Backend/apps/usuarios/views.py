from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from apps.usuarios.serializers import UsuarioSerializer
from apps.usuarios.models import Usuario

# Create your views here.

class UsuariolistAV(APIView):

    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer =  UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer =  UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetalleAV(APIView):
    def get(self, request, id):
        try: 
            usuarios = Usuario.objects.get(id=id)
            serializer =  UsuarioSerializer(usuarios)
            return Response(serializer.data)

        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try: 
            usuarios = Usuario.objects.get(id=id)
            serializer =  UsuarioSerializer(usuarios, data= request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):

        try: 
            usuarios = Usuario.objects.get(id=id)
            usuarios.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
