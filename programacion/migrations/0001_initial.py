# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0001_initial'),
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profesor', models.ForeignKey(to='profesor.Profesor')),
                ('programacion_actividad', models.ForeignKey(to='actividades.Actividad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
