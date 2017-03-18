# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0003_remove_programacion_servicio'),
        ('inscripcion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiantes',
            options={'verbose_name_plural': 'Estudiantes'},
        ),
        migrations.AlterModelOptions(
            name='programa',
            options={'verbose_name_plural': 'Programas'},
        ),
        migrations.RemoveField(
            model_name='estudiantes',
            name='inscripcion',
        ),
        migrations.RemoveField(
            model_name='inscripcion',
            name='actividad',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='estudiante',
            field=models.ForeignKey(to='inscripcion.Estudiantes', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='fecha_inscripcion',
            field=models.DateField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='programacion',
            field=models.ForeignKey(to='programacion.Programacion', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='Correo_Institucional',
            field=models.EmailField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='Programa_Academico',
            field=models.ForeignKey(to='inscripcion.Programa', null=True),
        ),
    ]
