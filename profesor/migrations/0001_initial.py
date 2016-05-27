# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('nombres', models.CharField(max_length=30)),
                ('id_ucc', models.PositiveSmallIntegerField(max_length=12, serialize=False, primary_key=True)),
                ('estado', models.CharField(max_length=20, choices=[(b'ACTIVO', b'Activo'), (b'INACTIVO', b'Inactivo')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
