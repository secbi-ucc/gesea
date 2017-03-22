# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diaactividad',
            options={'verbose_name_plural': 'Dia Actividad'},
        ),
        migrations.AlterModelOptions(
            name='lugar',
            options={'verbose_name_plural': 'Lugar'},
        ),
        migrations.AlterModelOptions(
            name='programacion',
            options={'verbose_name_plural': 'Programacion'},
        ),
    ]
