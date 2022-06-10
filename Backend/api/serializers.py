from rest_framework import serializers
from apps.semilleros.models import Semillero
from apps.usuarios.models import *
from apps.avals.models import *

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class Aval_semillero_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Aval_semillero
        fields = '__all__'

class Aval_usuario_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Aval_usuario
        fields = '__all__'


        
class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
   # aprobado_e = Aval_usuario_Serializer(many=True, read_only = True)
    rol = RolSerializer(many=True, read_only = True)
    idioma_u = IdiomaSerializer(many=True, read_only = True)
    cursos = CursoSerializer(many=True, read_only = True)
    class Meta:
        model = Usuario
        fields = '__all__'

class SemilleroSerializer(serializers.ModelSerializer):
   # aprobado_s = Aval_semillero_Serializer(many=True, read_only = True)
    usuarios = UsuarioSerializer(many=True, read_only = True)

    class Meta:
        model = Semillero
        fields = '__all__'
        
        # fields = [
        #     "id",
        #     "nombre",
        #     "facultad",
        #     "programa_academico",
        #     "investigacion",
        #     "investigacion_asociado",
        #     "tematica",
        #     "justificacion",
        # ]