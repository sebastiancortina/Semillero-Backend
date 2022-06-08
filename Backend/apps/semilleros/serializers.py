from rest_framework import serializers
from apps.semilleros.models import Semillero
 


class SemilleroSerializer(serializers.ModelSerializer):

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