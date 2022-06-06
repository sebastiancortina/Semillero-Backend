from rest_framework import serializers
from apps.semilleros.models import Semillero
 


class SemilleroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Semillero
        fields = [
            "id",
            "nombre",
            "facultad",
            "programa_academico",
            "investigacion",
            "investigacion_asociado",
            "tematica",
            "justificacion",
        ]