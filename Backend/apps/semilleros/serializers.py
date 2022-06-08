from rest_framework import serializers
from apps.semilleros.models import Semillero
from apps.usuarios.models import Usuario
#from apps.usuarios.serializers import UsuarioSerializer
#from apps.semilleros.serializers import SemilleroSerializer

class UsuarioSerializer(serializers.ModelSerializer):
   # usuariolist = SemilleroSerializer(many=True, read_only = True)
    class Meta:
        model = Usuario
        fields = '__all__'


class SemilleroSerializer(serializers.ModelSerializer):
    usuarioslist = UsuarioSerializer(many=True, read_only = True)
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