# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0004_auto_20170307_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiantes',
            name='inscripcion',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='estudiante',
            field=models.ForeignKey(to='inscripcion.Estudiantes', null=True),
            preserve_default=True,
        ),
    ]
