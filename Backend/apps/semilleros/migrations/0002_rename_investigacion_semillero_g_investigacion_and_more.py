# Generated by Django 4.0.4 on 2022-06-08 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semilleros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semillero',
            old_name='investigacion',
            new_name='g_investigacion',
        ),
        migrations.RenameField(
            model_name='semillero',
            old_name='investigacion_asociado',
            new_name='l_investigacion_asociado',
        ),
        migrations.AddField(
            model_name='semillero',
            name='activo',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
        migrations.AddField(
            model_name='semillero',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='semillero',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]