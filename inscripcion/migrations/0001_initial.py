# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('idEstudiante', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('semestre', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=30)),
                ('facultad', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('Horas_estudiante', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TipodeParticipacion', models.CharField(max_length=30, choices=[('Curso', 'Curso'), ('Grupo de representacion', 'Grupo de representacion'), ('Equipos de representacion', 'Equipos de representacion'), ('Brigada', 'Brigada'), ('Otro', 'Otro')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='inscripcion',
            field=models.ManyToManyField(to='inscripcion.Inscripcion'),
            preserve_default=True,
        ),
    ]
