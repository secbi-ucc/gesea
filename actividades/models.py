from django.db import models
#Modelo de la clase servicio
class Servicio(models.Model):
    Codigo_servicio = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.nombre)

#Modelo de la clase tipo de actividad
class TipoActividad(models.Model):
    Codigo_tipoActividad = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.nombre)

#Modelo de la clase actividad
class Actividad(models.Model):
    ESTADOS_ACTIVIDAD = (
        ('ABIERTA', 'Abierta'),
        ('CERRADA', 'Cerrada'),
    )
    servicio =  models.ForeignKey(Servicio)
    Codigo_actividad = models.CharField(max_length=10)
    tipo_actividad = models.ForeignKey(TipoActividad)
    Estado_actividad =  models.CharField(max_length=30, choices=ESTADOS_ACTIVIDAD, default='ABIERTA')
    Cupo_Actividad = models.IntegerField(max_length = 5)

    def __unicode__(self):
        return unicode(self.tipo_actividad)
