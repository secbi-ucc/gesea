from django.db import models
#Modelo de la clase servicio
class Servicio(models.Model):
    NOMBRES_SERVICIOS = (
        ('PROMOCION DE LA SALUD', 'Promocion de la salud'),
        ('DEPORTES', 'Deportes'),
        ('PATRIMONIO CULTURAL', 'Patrimonio cultural'),
        ('ORIENTACION Y ACOMPANAMIENTO', 'Orientacion y acompanamiento'),
    )
    Codigo_servicio = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=50, choices=NOMBRES_SERVICIOS)

    def __unicode__(self):
        return unicode(self.nombre)

#Modelo de la clase actividad
class Actividad(models.Model):

    ESTADOS_ACTIVIDAD = (
        ('ABIERTA', 'Abierta'),
        ('CERRADA', 'Cerrada'),
    )
    Codigo_actividad = models.CharField(max_length=10, unique=True)
    tipo_actividad = models.CharField(max_length=80)
    Estado_actividad =  models.CharField(max_length=30, choices=ESTADOS_ACTIVIDAD, default='ABIERTA')
    Cupo_Actividad = models.IntegerField()
    class Meta:
        verbose_name_plural = "Actividades"
    def __unicode__(self):
        return unicode(self.tipo_actividad)

#Modelo de la clase registro de actividad
class RegistroActividad(models.Model):
    servicio =  models.ForeignKey(Servicio)
    actividad =  models.ForeignKey(Actividad)
    class Meta:
        verbose_name_plural = "Registro Actividad"

    def __unicode__(self):
        return unicode(self.actividad)
