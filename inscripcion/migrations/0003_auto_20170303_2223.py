# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0002_auto_20170303_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='Correo_Institucional',
            field=models.EmailField(unique=True, max_length=50),
        ),
    ]
