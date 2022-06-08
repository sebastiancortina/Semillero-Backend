from rest_framework import serializers
#from apps.semilleros.serializers import SemilleroSerializer
from apps.usuarios.models import Usuario
#from apps.semilleros.models import Semillero
"""
class SemilleroSerializer(serializers.ModelSerializer):
    #id_usuario_5 = UsuarioSerializer(many=True, read_only = True)
    class Meta:
        model = Semillero
        fields = '__all__'
"""

class UsuarioSerializer(serializers.ModelSerializer):
   # usuariolist = SemilleroSerializer(many=True, read_only = True)
    class Meta:
        model = Usuario
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