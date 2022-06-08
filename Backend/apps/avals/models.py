from django.db import models
from apps.semilleros.models import Semillero
from apps.usuarios.models import Usuario


# Create your models here.
class Aval(models.Model):
    id_semillero = models.OneToOneField(Semillero, on_delete=models.CASCADE, related_name="id_semillero_1", null=True, blank=True )
    id_usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="id_usuario", null=True, blank=True )
    observaciones_s =  models.TextField('OBSERVACION S', null=True, blank=True)
    observaciones_u =  models.TextField('OBSERVACION U', null=True, blank=True)
    firma_d = models.CharField('DECANO /COMITÉ DE INV. DE LA FACULTAD', max_length=250, null=True, blank=True)
    probado_d = models.BooleanField(default=False)
    firma_v = models.CharField('VICERRECTOR DE INVESTIGACIONES U HOMÓLOGO EN SEDE', max_length=250, null=True, blank=True)
    probado_v = models.BooleanField(default=False)
    firma_c = models.CharField('DOCENTE COORDINADOR DEL SEMILLERO', max_length=250, null=True, blank=True)
    probado_c = models.BooleanField(default=False)
    firma_r = models.CharField('Firma Recibido', max_length=250, null=True, blank=True)
    probado_r = models.BooleanField(default=False)
    activo = models.BooleanField('ACTIVO', default=False)

    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)


