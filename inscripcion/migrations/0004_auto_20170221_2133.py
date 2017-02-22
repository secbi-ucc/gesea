# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0003_auto_20170221_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiantes',
            name='Horas_estudiante',
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='ciclo_lectivo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='genero',
            field=models.CharField(max_length=30, null=True, choices=[('F', 'Femenino'), ('M', 'Masculino')]),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='telefono',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
