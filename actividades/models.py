from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre
class TipoActividad(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Actividad(models.Model):
    tipo_actividad = models.ForeignKey(TipoActividad)
    servicio = models.ForeignKey(Servicio)

    def __unicode__(self):
        return self.tipo_actividad.nombre
