# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0002_auto_20161031_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='Nombre',
            field=models.CharField(default='hola', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicio',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='tipoactividad',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
