# Generated by Django 4.0.4 on 2022-06-09 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_alter_lider_id_usuario_alter_usuario_id_semillero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lider',
            name='id_usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lider', to='usuarios.usuario'),
        ),
    ]
