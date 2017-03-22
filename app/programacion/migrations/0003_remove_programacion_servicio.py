# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0002_auto_20170307_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programacion',
            name='Servicio',
        ),
    ]
