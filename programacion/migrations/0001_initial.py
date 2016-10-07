# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
        ('profesor', '0001_initial'),
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
                ('NombreLugar', models.CharField(max_length=30, choices=[(b'Canchas Deportivas', b'Canchas Deportiva'), (b'Teatrino', b'Teatrino'), (b'Cafeteria', b'Cafeteria'), (b'Auditorio', b'Auditorio'), (b'7mo Piso', b'7mo Piso'), (b'1mo Piso', b'1mo Piso'), (b'Otro', b'Otro')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TipodeParticipacion', models.CharField(max_length=30, choices=[(b'Curso', b'Curso'), (b'Grupo de representacion', b'Grupo de representacion'), (b'Equipos de representacion', b'Equipos de representacion'), (b'Brigada', b'Brigada'), (b'Otro', b'Otro')])),
                ('Fecha_Inicio', models.DateTimeField(null=True)),
                ('Fecha_Final', models.DateTimeField(null=True)),
                ('Dia_semana', models.ManyToManyField(to='programacion.DiaActividad')),
                ('Servicio', models.ForeignKey(to='actividades.Servicio')),
                ('actividad', models.ForeignKey(to='actividades.Actividad')),
                ('lugarActividad', models.ForeignKey(to='programacion.Lugar')),
                ('profesor', models.ForeignKey(to='profesor.Profesor')),
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
