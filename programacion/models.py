from django.db import models
from profesor.models import Profesor
from inscripcion.models import Inscripcion
from actividades.models import Actividad ,Servicio
from django.utils import timezone

class Horario(models.Model):
    Hora_inicio = models.TimeField(blank=True, null=True)
    Hora_Final = models.TimeField(blank=True, null=True)
    Fecha_Inicio = models.DateField(blank=True, null=True)
    Fecha_Final = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.Hora_inicio)


class Lugar(models.Model):
    Lugar_Actividad = (
        ('Canchas Deportivas', 'Canchas Deportiva'),
        ('Teatrino', 'Teatrino'),
        ('Cafeteria', 'Cafeteria'),
        ('Auditorio', 'Auditorio'),
        ('7mo Piso', '7mo Piso'),
        ('Otro', 'Otro'),
    )
    NombreLugar = models.CharField(max_length=30, choices=Lugar_Actividad)

    def __unicode__(self):
        return unicode(self.NombreLugar)

class Programacion(models.Model):
    profesor = models.ForeignKey(Profesor)
    lugarActividad = models.ForeignKey(Lugar)
    Servicio = models.ForeignKey(Servicio)
    inscripcion = models.ForeignKey(Inscripcion)
    actividad = models.ForeignKey(Actividad)
    horario = models.ForeignKey(Horario)

    def __unicode__(self):
        return unicode(self.actividad)
