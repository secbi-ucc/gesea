# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0001_initial'),
        ('inscripcion', '0004_auto_20170221_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='InscripcionEstudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inscripcion', models.DateField(auto_now=True)),
                ('actividad', models.ForeignKey(to='programacion.Programacion')),
                ('estudiante', models.ForeignKey(to='inscripcion.Estudiantes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
