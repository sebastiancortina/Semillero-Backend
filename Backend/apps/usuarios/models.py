from django.db import models
from apps.semilleros.models import Semillero

# Create your models here.
class Usuario(models.Model):
    ni = models.BigIntegerField(primary_key=True)
    nombre = models.CharField('NOMBRE COMPLETO', max_length=250)
    fecha_n = models.CharField('FECHA DE NACIMIENTO', max_length=250)
    direccion = models.CharField('DIRECCIÓN RESIDENCIA', max_length=250)
    email = models.EmailField('CORREO ELECTRÓNICO', max_length=250)
    l_espedicion = models.CharField('LUGAR DE EXPEDICIÓN ID', max_length=250)
    l_nacimiento = models.CharField('LUGAR DE NACIMIENTO', max_length=250)
    telefono = models.BigIntegerField('TELÉFONO/ CELULAR')
    n_emergencia = models.CharField('EN CASO DE EMERGENCIA LLAMAR A', max_length=250)
    numero_emergencia = models.CharField('NÚMERO DE CONTACTO', max_length=250) #
    activo = models.BooleanField('ACTIVO', default=True)
    id_semillero = models.ForeignKey(Semillero, on_delete=models.CASCADE, related_name="usuarioslist" )
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ni)   

class Idioma(models.Model):
    lengua = models.CharField('LENGUA', max_length=250,  null=True, blank=True)
    nivel = models.CharField('NIVEL', max_length=250,  null=True, blank=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="id_usuario_1" )

    def __str__(self):
        return self.lengua 


class Lider(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="id_usuario_2" )

    def __str__(self):
        return str(self.id_usuario)

class Rol(models.Model):
    rol = models.CharField('Rol',max_length=250)
    programa = models.CharField('Programa', max_length=250, null=True, blank=True)
    año_i = models.CharField('AÑO INGRESO', max_length=250,  null=True, blank=True)
    semestre_a = models.CharField('SEMESTRE ACTUAL', max_length=250,  null=True, blank=True)
    f_grado =  models.CharField('FECHA DE GRADO', max_length=250,  null=True, blank=True)
    pregrado = models.CharField('PREGRADO', max_length=250, null=True, blank=True)
    posgrado = models.CharField('POSGRADOS', max_length=250, null=True, blank=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="id_usuario_3")

    def __str__(self):
        return str( self.id_usuario)  

class Curso(models.Model):
    tematica = models.CharField('TEMATICA', max_length=250,  null=True, blank=True)
    institucion = models.CharField('INSTITUCION', max_length=250,  null=True, blank=True)
    t_vinculacion = models.CharField('TIPO DE VINCULACION', max_length=250,  null=True, blank=True)
    año =  models.CharField('AÑO', max_length=250,  null=True, blank=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="id_usuario_4" )

    def __str__(self):
        return self.tematica 