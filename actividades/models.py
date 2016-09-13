from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return unicode(self.nombre)


class TipoActividad(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.nombre)


class Actividad(models.Model):
    ESTADOS_ACTIVIDAD = (
        ('ACTIVA', 'Activa'),
        ('INACTIVA', 'Inactiva'),
    )
    servicio = models.ForeignKey(Servicio)
    tipo_actividad = models.ForeignKey(TipoActividad)
    Estado_actividad =  models.CharField(max_length=30, choices=ESTADOS_ACTIVIDAD, default='INACTIVA')

    def __unicode__(self):
        return unicode(self.tipo_actividad)
