# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0006_inscripcion_fecha_inscripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscripcion',
            old_name='actividad',
            new_name='programacion',
        ),
    ]
