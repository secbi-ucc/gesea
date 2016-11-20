# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0002_auto_20161113_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='inscripcion',
            field=models.ManyToManyField(to=b'inscripcion.Inscripcion', null=True, blank=True),
        ),
    ]
