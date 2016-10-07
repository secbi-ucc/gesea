# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Codigo_actividad', models.CharField(max_length=10)),
                ('Estado_actividad', models.CharField(default=b'ABIERTA', max_length=30, choices=[(b'ABIERTA', b'Abierta'), (b'CERRADA', b'Cerrada')])),
                ('Cupo_Actividad', models.IntegerField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Codigo_servicio', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoActividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Codigo_tipoActividad', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='actividad',
            name='servicio',
            field=models.ForeignKey(to='actividades.Servicio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='tipo_actividad',
            field=models.ForeignKey(to='actividades.TipoActividad'),
            preserve_default=True,
        ),
    ]
