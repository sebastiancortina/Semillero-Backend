# Generated by Django 4.0.4 on 2022-06-08 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semilleros', '0003_rename_l_investigacion_asociado_semillero_l_i_asociado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semillero',
            old_name='g_investigacion',
            new_name='g_in',
        ),
        migrations.AlterField(
            model_name='semillero',
            name='programa_academico',
            field=models.CharField(max_length=250, verbose_name='PROGRAMA ACADÉMICO'),
        ),
    ]
