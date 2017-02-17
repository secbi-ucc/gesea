# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiantes',
            old_name='sexo',
            new_name='genero',
        ),
    ]
