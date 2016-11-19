from __future__ import unicode_literals
from django.db import models
from programacion.models import Programacion
from actividades.models import Actividad


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
    SEMESTRE_ESTUDIANTE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )
    GENERO_ESTUDIANTE = (
        ('FEMENINO', 'Femenino'),
        ('MASCULINO', 'Masculino'),
    )
    FACULTAD_ESTUDIANTE = (
        ('CONTADURIA PUBLICA', 'Contaduria publica'),
        ('DERECHO', 'Derecho'),
        ('INGENIERIA DE SISTEMAS', 'Ingenieria de sistemas'),
        ('PSICOLOGIA', 'Psicologia'),
    )
    Codigo_estudiante = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    semestre = models.CharField(max_length=30 , choices=SEMESTRE_ESTUDIANTE)
    sexo = models.CharField(max_length=30, choices=GENERO_ESTUDIANTE)
    facultad = models.CharField(max_length=30, choices=FACULTAD_ESTUDIANTE)
    correo = models.CharField(max_length=30, unique=True)
    telefono = models.CharField(max_length=30)
    Horas_estudiante = models.IntegerField()
    inscripcion = models.ManyToManyField(Inscripcion)
    Estado = models.CharField(max_length=20, choices=ESTADOS_ESTUDIANTE, default='ACTIVO')

    def __unicode__(self):
        return unicode(self.nombre)
