# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('ID_Estudiante', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('Primer_Nombre', models.CharField(max_length=30, null=True)),
                ('Segundo_Nombre', models.CharField(max_length=30, null=True)),
                ('Primer_Apellido', models.CharField(max_length=30, null=True)),
                ('Segundo_Apellido', models.CharField(max_length=30, null=True)),
                ('Nro_Documento', models.CharField(max_length=30)),
                ('Tipo_Documento', models.CharField(max_length=30, choices=[('TI', 'TI'), ('CC', 'CC')])),
                ('genero', models.CharField(max_length=30, null=True, choices=[('F', 'Femenino'), ('M', 'Masculino')])),
                ('Correo_Institucional', models.EmailField(unique=True, max_length=30)),
                ('Nro_Telefonico', models.CharField(max_length=30, null=True)),
                ('Ciclo_Lectivo', models.CharField(max_length=30, null=True)),
                ('Descripcion', models.CharField(max_length=30, null=True)),
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
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='Programa_Academico',
            field=models.ForeignKey(to='inscripcion.Programa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='inscripcion',
            field=models.ManyToManyField(to='inscripcion.Inscripcion', null=True, blank=True),
            preserve_default=True,
        ),
    ]
