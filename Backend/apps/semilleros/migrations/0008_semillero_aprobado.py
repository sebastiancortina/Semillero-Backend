# Generated by Django 4.0.4 on 2022-06-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semilleros', '0007_remove_semillero_id_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='semillero',
            name='aprobado',
            field=models.BooleanField(default=False, verbose_name='Aprobacion'),
        ),
    ]
