# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0005_inscripcionestudiante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcionestudiante',
            name='actividad',
            field=models.ForeignKey(to='actividades.Actividad', null=True),
        ),
    ]
