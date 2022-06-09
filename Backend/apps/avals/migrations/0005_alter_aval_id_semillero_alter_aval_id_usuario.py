# Generated by Django 4.0.4 on 2022-06-09 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semilleros', '0008_semillero_aprobado'),
        ('usuarios', '0010_usuario_aprobado'),
        ('avals', '0004_remove_aval_firma_c_remove_aval_firma_d_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aval',
            name='id_semillero',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aprobado_s', to='semilleros.semillero'),
        ),
        migrations.AlterField(
            model_name='aval',
            name='id_usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aprobado_e', to='usuarios.usuario'),
        ),
    ]