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
                ('Codigo_estudiante', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('nid', models.CharField(max_length=30)),
                ('tipo_nid', models.CharField(max_length=30, choices=[('TI', 'TI'), ('CC', 'CC')])),
                ('semestre', models.CharField(blank=True, max_length=30, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])),
                ('sexo', models.CharField(max_length=30, choices=[('F', 'Femenino'), ('M', 'Masculino')])),
                ('programa_academico', models.CharField(max_length=30)),
                ('correo', models.EmailField(unique=True, max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('Horas_estudiante', models.IntegerField()),
                ('Estado', models.CharField(default='ACTIVO', max_length=20, choices=[('ACTIVO', 'Activo'), ('INACTIVO', 'Inactivo')])),
                ('ciclo_lectivo', models.CharField(max_length=30)),
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
            field=models.ManyToManyField(to='inscripcion.Inscripcion', null=True, blank=True),
            preserve_default=True,
        ),
    ]
