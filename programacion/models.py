from django.db import models
from actividades.models import Actividad ,Area
from django.utils import timezone
from datetime import datetime, date

class Horario(models.Model):
    Hora_Inicio = models.TimeField(null=True)
    Hora_Final = models.TimeField(null=True)
    class Meta:
        verbose_name_plural = "Horas"

    def get_time_diff(self):
        timediff = datetime.combine(date.min,  self.Hora_Final) - datetime.combine(date.min, self.Hora_Inicio)
        return str(timediff)[:1]

    def __unicode__(self):
        return unicode(str(self.Hora_Inicio) + " - " + str(self.Hora_Final))


class Lugar(models.Model):
    NombreLugar = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "Lugares"
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
    class Meta:
        verbose_name_plural = "Dias Actividades"

    def __unicode__(self):
        return unicode(self.Dia_Actividad + "-" +  str(self.Horario))


class Programacion(models.Model):
    actividad = models.ForeignKey(Actividad)
    Tipo_participacion = (
        ('CURSO', 'Curso'),
        ('GRUPO DE REPRESENTACION', 'Grupo de representacion'),
        ('EQUIPOS DE REPRESENTACION', 'Equipos de representacion'),
        ('BRIGADA', 'Brigada'),
        ('OTRO', 'Otro'),
    )
    TipodeParticipacion = models.CharField(max_length=30, choices=Tipo_participacion)
    Instructor = models.ForeignKey('inscripcion.Instructor', null=True, blank=True)
    lugarActividad = models.ForeignKey(Lugar)
    Dia_semana =  models.ManyToManyField(DiaActividad)
    Fecha_Inicio = models.DateTimeField(null=True)
    Fecha_Final = models.DateTimeField(null=True)

    def horario(self):
        return ",".join([str(p) for p in self.Dia_semana.all()])

    class Meta:
        verbose_name_plural = "Actividades Programadas"
        verbose_name = "Actividad pogramada"

    def __unicode__(self):
        return unicode(self.actividad)
