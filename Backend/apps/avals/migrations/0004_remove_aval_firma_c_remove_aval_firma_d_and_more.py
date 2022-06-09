# Generated by Django 4.0.4 on 2022-06-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avals', '0003_aval_probado_c_aval_probado_d_aval_probado_r_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aval',
            name='firma_c',
        ),
        migrations.RemoveField(
            model_name='aval',
            name='firma_d',
        ),
        migrations.RemoveField(
            model_name='aval',
            name='firma_r',
        ),
        migrations.RemoveField(
            model_name='aval',
            name='firma_v',
        ),
        migrations.RemoveField(
            model_name='aval',
            name='observaciones_s',
        ),
        migrations.RemoveField(
            model_name='aval',
            name='observaciones_u',
        ),
        migrations.RemoveField(
            model_name='aval',
            name='probado_c',
        ),
        migrations.RemoveField(
            model_name='aval',
            name='probado_d',
        ),
        migrations.RemoveField(
            model_name='aval',
            name='probado_r',
        ),
        migrations.RemoveField(
            model_name='aval',
            name='probado_v',
        ),
        migrations.AddField(
            model_name='aval',
            name='aprobado',
            field=models.BooleanField(default=False, verbose_name='Aprobacion'),
        ),
        migrations.AlterField(
            model_name='aval',
            name='activo',
            field=models.BooleanField(verbose_name='ACTIVO'),
        ),
    ]