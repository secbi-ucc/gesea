from __future__ import unicode_literals
from django.db import models
from programacion.models import Programacion


# Create your models here.

class Inscripcion(models.Model):
    actividad = models.ForeignKey(Programacion)
    def __unicode__(self):
        return unicode(self.actividad)


class Estudiantes(models.Model):
    ESTADOS_ESTUDIANTE = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    Codigo_estudiante = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    semestre = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30)
    facultad = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    Horas_estudiante = models.IntegerField()
    inscripcion = models.ManyToManyField(Inscripcion)
    Estado = models.CharField(max_length=20, choices=ESTADOS_ESTUDIANTE, default='ACTIVO')

    def __unicode__(self):
        return unicode(self.nombre)
