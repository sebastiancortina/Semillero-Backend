# Generated by Django 4.0.4 on 2022-06-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Semillero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='NOMBRE DEL SEMILLERO')),
                ('facultad', models.CharField(max_length=250, verbose_name='FACULTAD')),
                ('programa_academico', models.CharField(max_length=250, verbose_name='PROGRMA ACADÉMICO')),
                ('investigacion', models.CharField(max_length=250, verbose_name='GRUPO DE INVESTIGACIÓN AL CUAL ESTÁ VINCULADO EL SEMILLERO')),
                ('investigacion_asociado', models.CharField(max_length=250, verbose_name='LÍNEA Y SUBLÍNEA DE INVESTIGACIÓN ASOCIADOS')),
                ('tematica', models.CharField(max_length=250, verbose_name='TÉMATICA DE ESTUDIO DEL SEMILLERO')),
                ('justificacion', models.TextField(max_length=2000, verbose_name=' JUSTIFICACIÓN DEL SEMILLERO DE INVESTIGACIÓN')),
            ],
        ),
    ]
