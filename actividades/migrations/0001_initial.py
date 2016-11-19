# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Codigo_actividad', models.CharField(unique=True, max_length=10)),
                ('Estado_actividad', models.CharField(default=b'ABIERTA', max_length=30, choices=[(b'ABIERTA', b'Abierta'), (b'CERRADA', b'Cerrada')])),
                ('Cupo_Actividad', models.IntegerField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Codigo_servicio', models.CharField(unique=True, max_length=10)),
                ('nombre', models.CharField(max_length=50, choices=[(b'PROMOCION DE LA SALUD', b'Promocion de la salud'), (b'DEPORTES', b'Deportes'), (b'PATRIMONIO CULTURAL', b'Patrimonio cultural'), (b'ORIENTACION Y ACOMPANAMIENTO', b'Orientacion y acompanamiento')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoActividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Codigo_tipoActividad', models.CharField(unique=True, max_length=10)),
                ('nombre', models.CharField(max_length=50, choices=[(b'ATENCION PSICOLOGICA', b'Atencion psicologica'), (b'ATENCION PSICOSOCIAL', b'Atencion psicosocial '), (b'CONSEJERIAS', b'Consejerias'), (b'DANZA', b'Danza'), (b'FUTBOL 11', b'Futbol 11'), (b'GESTION AMBIENTAL', b'Gestion ambiental'), (b'MEDICINA GENERAL', b'Medicina general'), (b'MICROFUTBOL', b'Microfutbol Masc Y Fem'), (b'MUSICA', b'Musica'), (b'ORIENTACION ESPIRITUAL-CONVIVENCIA', b'Orientacion espiritual- convivencia'), (b'PRIMEROS AUXILIOS', b'Primeros auxilios'), (b'PROMOCIONES SOCIOECONOMICAS', b'promociones socioeconomicas'), (b'SOFTBOL', b'Softbol'), (b'TEATRO', b'Teatro'), (b'TORNEO EMPRESARIAL MINIFUTBOL', b'Torneo Empresarial Mini Futbol'), (b'TORNEO INTERNO MICRO', b'Torneo Interno Micro'), (b'VOLEIBOL', b'Voleibol Masc Y Fem')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='actividad',
            name='servicio',
            field=models.ForeignKey(to='actividades.Servicio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='tipo_actividad',
            field=models.ForeignKey(to='actividades.TipoActividad'),
            preserve_default=True,
        ),
    ]
