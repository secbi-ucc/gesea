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
    Lugar_Actividad = (
        ('Canchas Deportivas', 'Canchas Deportiva'),
        ('Teatrino', 'Teatrino'),
        ('Cafeteria', 'Cafeteria'),
        ('Auditorio', 'Auditorio'),
        ('7mo Piso', '7mo Piso'),
        ('1mo Piso', '1mo Piso'),
        ('Otro', 'Otro'),
    )
    NombreLugar = models.CharField(max_length=30, choices=Lugar_Actividad)

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
        ('Curso', 'Curso'),
        ('Grupo de representacion', 'Grupo de representacion'),
        ('Equipos de representacion', 'Equipos de representacion'),
        ('Brigada', 'Brigada'),
        ('Otro', 'Otro'),
    )
    TipodeParticipacion = models.CharField(max_length=30, choices=Tipo_participacion)
    profesor = models.ForeignKey(Profesor)
    lugarActividad = models.ForeignKey(Lugar)
    Servicio = models.ForeignKey(Servicio)
    actividad = models.ForeignKey(Actividad)
    Dia_semana =  models.ManyToManyField(DiaActividad)
    Fecha_Inicio = models.DateTimeField(null=True)
    Fecha_Final = models.DateTimeField(null=True)

    def __unicode__(self):
        return unicode(self.actividad)
