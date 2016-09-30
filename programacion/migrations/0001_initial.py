# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0001_initial'),
        ('actividades', '0001_initial'),
        ('profesor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Fecha_Inicio', models.DateTimeField(null=True)),
                ('Fecha_Final', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NombreLugar', models.CharField(max_length=30, choices=[(b'Canchas Deportivas', b'Canchas Deportiva'), (b'Teatrino', b'Teatrino'), (b'Cafeteria', b'Cafeteria'), (b'Auditorio', b'Auditorio'), (b'7mo Piso', b'7mo Piso'), (b'Otro', b'Otro')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Servicio', models.ForeignKey(to='actividades.Servicio')),
                ('actividad', models.ForeignKey(to='actividades.Actividad')),
                ('horario', models.ForeignKey(to='programacion.Horario')),
                ('inscripcion', models.ForeignKey(to='inscripcion.Inscripcion')),
                ('lugarActividad', models.ForeignKey(to='programacion.Lugar')),
                ('profesor', models.ForeignKey(to='profesor.Profesor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
