# Generated by Django 4.0.4 on 2022-06-09 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avals', '0002_alter_aval_firma_c_alter_aval_firma_d_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aval',
            name='probado_c',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aval',
            name='probado_d',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aval',
            name='probado_r',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aval',
            name='probado_v',
            field=models.BooleanField(default=False),
        ),
    ]
