# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='Identificacion',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='id_ucc',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
