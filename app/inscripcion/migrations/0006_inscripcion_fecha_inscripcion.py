# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0005_auto_20170307_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcion',
            name='fecha_inscripcion',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
