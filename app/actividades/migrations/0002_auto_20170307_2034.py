# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividad',
            options={'verbose_name_plural': 'Actividad'},
        ),
        migrations.AlterModelOptions(
            name='tipoactividad',
            options={'verbose_name_plural': 'Tipo Actividad'},
        ),
    ]
