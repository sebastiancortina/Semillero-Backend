# Generated by Django 4.0.4 on 2022-06-10 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semilleros', '0009_remove_semillero_aprobado'),
    ]

    operations = [
        migrations.AddField(
            model_name='semillero',
            name='aprobado',
            field=models.BooleanField(default=False, verbose_name='Aprobacion'),
        ),
    ]