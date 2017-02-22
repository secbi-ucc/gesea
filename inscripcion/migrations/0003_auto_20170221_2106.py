# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0002_auto_20170216_2105'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='estudiantes',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='estudiantes',
            name='nombre',
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='apellido_1',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='apellido_2',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='nombre_1',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='nombre_2',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='programa_academico',
            field=models.ForeignKey(to='inscripcion.Programa'),
        ),
    ]
