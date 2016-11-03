# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='Codigo_actividad',
            field=models.CharField(unique=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='Codigo_servicio',
            field=models.CharField(unique=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='tipoactividad',
            name='Codigo_tipoActividad',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
