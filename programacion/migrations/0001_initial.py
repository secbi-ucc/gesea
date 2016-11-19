# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '__first__'),
        ('profesor', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaActividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Dia_Actividad', models.CharField(max_length=10, choices=[(b'LUNES', b'Lunes'), (b'MARTES', b'Martes'), (b'MIERCOLES', b'Miercoles'), (b'JUEVES', b'Jueves'), (b'VIERNES', b'Viernes'), (b'SABADO', b'Sabado'), (b'DOMINGO', b'Domingo')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Hora_Inicio', models.TimeField(null=True)),
                ('Hora_Final', models.TimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NombreLugar', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TipodeParticipacion', models.CharField(max_length=30, choices=[(b'CURSO', b'Curso'), (b'GRUPO DE REPRESENTACION', b'Grupo de representacion'), (b'EQUIPOS DE REPRESENTACION', b'Equipos de representacion'), (b'BRIGADA', b'Brigada'), (b'OTRO', b'Otro')])),
                ('Fecha_Inicio', models.DateTimeField(null=True)),
                ('Fecha_Final', models.DateTimeField(null=True)),
                ('Dia_semana', models.ManyToManyField(to='programacion.DiaActividad')),
                ('Servicio', models.ForeignKey(to='actividades.Servicio')),
                ('actividad', models.ForeignKey(to='actividades.Actividad')),
                ('lugarActividad', models.ForeignKey(to='programacion.Lugar')),
                ('profesor', models.ForeignKey(blank=True, to='profesor.Profesor', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='diaactividad',
            name='Horario',
            field=models.ForeignKey(to='programacion.Horario'),
            preserve_default=True,
        ),
    ]
