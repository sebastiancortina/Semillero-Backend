# Generated by Django 4.0.4 on 2022-06-09 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_usuario_aprobado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='usuarios.usuario'),
        ),
    ]
