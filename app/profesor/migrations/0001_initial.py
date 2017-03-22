# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id_ucc', models.IntegerField(serialize=False, primary_key=True)),
                ('Identificacion', models.IntegerField(unique=True)),
                ('estado', models.CharField(default=b'ACTIVO', max_length=20, choices=[(b'ACTIVO', b'Activo'), (b'INACTIVO', b'Inactivo')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
