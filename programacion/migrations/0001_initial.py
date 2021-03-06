# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaActividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dia_Actividad', models.CharField(choices=[(b'LUNES', b'Lunes'), (b'MARTES', b'Martes'), (b'MIERCOLES', b'Miercoles'), (b'JUEVES', b'Jueves'), (b'VIERNES', b'Viernes'), (b'SABADO', b'Sabado'), (b'DOMINGO', b'Domingo')], max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Dias Actividades',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hora_Inicio', models.TimeField(null=True)),
                ('Hora_Final', models.TimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Horas',
            },
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreLugar', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Lugares',
            },
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipodeParticipacion', models.CharField(choices=[(b'CURSO', b'Curso'), (b'GRUPO DE REPRESENTACION', b'Grupo de representacion'), (b'EQUIPOS DE REPRESENTACION', b'Equipos de representacion'), (b'BRIGADA', b'Brigada'), (b'OTRO', b'Otro')], max_length=30)),
                ('Fecha_Inicio', models.DateTimeField(null=True)),
                ('Fecha_Final', models.DateTimeField(null=True)),
                ('Dia_semana', models.ManyToManyField(to='programacion.DiaActividad')),
                #('Instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profesor.Instructor')),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.Actividad')),
                ('lugarActividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programacion.Lugar')),
            ],
            options={
                'verbose_name': 'Actividad pogramada',
                'verbose_name_plural': 'Actividades Programadas',
            },
        ),
        migrations.AddField(
            model_name='diaactividad',
            name='Horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programacion.Horario'),
        ),
    ]
