from django.db import models
from profesor.models import Profesor
from actividades.models import Actividad ,Servicio
from django.utils import timezone

class Horario(models.Model):
    Hora_Inicio = models.TimeField(null=True)
    Hora_Final = models.TimeField(null=True)

    def __unicode__(self):
        return unicode(self.Hora_Inicio)


class Lugar(models.Model):
    NombreLugar = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.NombreLugar)

class DiaActividad(models.Model):
    Diaactidad = (
        ('LUNES', 'Lunes'),
        ('MARTES', 'Martes'),
        ('MIERCOLES', 'Miercoles'),
        ('JUEVES', 'Jueves'),
        ('VIERNES', 'Viernes'),
        ('SABADO', 'Sabado'),
        ('DOMINGO', 'Domingo'),
    )

    Dia_Actividad = models.CharField(max_length=10,choices=Diaactidad)
    Horario =  models.ForeignKey(Horario)

    def __unicode__(self):
        return unicode(self.Dia_Actividad)


class Programacion(models.Model):
    Tipo_participacion = (
        ('CURSO', 'Curso'),
        ('GRUPO DE REPRESENTACION', 'Grupo de representacion'),
        ('EQUIPOS DE REPRESENTACION', 'Equipos de representacion'),
        ('BRIGADA', 'Brigada'),
        ('OTRO', 'Otro'),
    )
    TipodeParticipacion = models.CharField(max_length=30, choices=Tipo_participacion)
    profesor = models.ForeignKey(Profesor, null=True, blank=True)
    lugarActividad = models.ForeignKey(Lugar)
    Servicio = models.ForeignKey(Servicio)
    actividad = models.ForeignKey(Actividad)
    Dia_semana =  models.ManyToManyField(DiaActividad)
    Fecha_Inicio = models.DateTimeField(null=True)
    Fecha_Final = models.DateTimeField(null=True)

    def __unicode__(self):
        return unicode(self.actividad)
