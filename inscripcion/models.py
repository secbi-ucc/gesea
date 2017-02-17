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
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    TIPO_NID = (
        ('TI', 'TI'),
        ('CC', 'CC'),
    )

    Codigo_estudiante = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    nid = models.CharField(max_length=30)
    tipo_nid=models.CharField(max_length=30, choices=TIPO_NID)
    semestre = models.CharField(max_length=30 , choices=SEMESTRE_ESTUDIANTE, blank=True)
    genero = models.CharField(max_length=30, choices=GENERO_ESTUDIANTE)
    programa_academico = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30, unique=True)
    telefono = models.CharField(max_length=30)
    Horas_estudiante = models.IntegerField()
    inscripcion = models.ManyToManyField(Inscripcion, null=True, blank=True)
    Estado = models.CharField(max_length=20, choices=ESTADOS_ESTUDIANTE, default='ACTIVO')
    ciclo_lectivo = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.nombre)
