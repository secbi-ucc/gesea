# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiantes',
            name='id',
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='Codigo_estudiante',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
    ]
