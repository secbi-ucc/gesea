# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Codigo_estudiante', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('semestre', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=30)),
                ('facultad', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('Horas_estudiante', models.IntegerField()),
                ('Estado', models.CharField(default='ACTIVO', max_length=20, choices=[('ACTIVO', 'Activo'), ('INACTIVO', 'Inactivo')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actividad', models.ForeignKey(to='programacion.Programacion')),
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
