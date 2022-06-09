from rest_framework import serializers
from apps.semilleros.models import Semillero
from apps.usuarios.models import *

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    rol = RolSerializer(many=True, read_only = True)
    idioma_u = IdiomaSerializer(many=True, read_only = True)
    class Meta:
        model = Usuario
        fields = '__all__'

class SemilleroSerializer(serializers.ModelSerializer):
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