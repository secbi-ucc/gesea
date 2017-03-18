from django.db import models
from profesor.models import Profesor
from actividades.models import Actividad ,Servicio
from django.utils import timezone

class Horario(models.Model):
    Hora_Inicio = models.TimeField(null=True)
    Hora_Final = models.TimeField(null=True)

    def __unicode__(self):
        return unicode(str(self.Hora_Inicio) + " - " + str(self.Hora_Final))


class Lugar(models.Model):
    NombreLugar = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "Lugar"
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
        verbose_name_plural = "Dia Actividad"

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
    profesor = models.ForeignKey(Profesor, null=True, blank=True)
    lugarActividad = models.ForeignKey(Lugar)
    Dia_semana =  models.ManyToManyField(DiaActividad)
    Fecha_Inicio = models.DateTimeField(null=True)
    Fecha_Final = models.DateTimeField(null=True)

    def horario(self):
        return ",".join([str(p) for p in self.Dia_semana.all()])

    class Meta:
        verbose_name_plural = "Programacion"
    def __unicode__(self):
        return unicode(self.actividad)
