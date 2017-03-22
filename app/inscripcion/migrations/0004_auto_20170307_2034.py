# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0003_auto_20170303_2223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiantes',
            options={'verbose_name_plural': 'Estudiantes'},
        ),
        migrations.AlterModelOptions(
            name='inscripcion',
            options={'verbose_name_plural': 'Inscripcion'},
        ),
        migrations.AlterModelOptions(
            name='programa',
            options={'verbose_name_plural': 'Programas'},
        ),
    ]
