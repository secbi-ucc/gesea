from __future__ import unicode_literals
from django.db import models
from programacion.models import Programacion
from actividades.models import Actividad


# Create your models here.
class Inscripcion(models.Model):
    actividad = models.ForeignKey(Programacion)
    def __unicode__(self):
        return unicode(self.actividad)


class Programa(models.Model):
    cod = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)

    def __unicode__(self):
        return unicode(self.nombre)


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
    nombre_1 = models.CharField(max_length=30, null=True)
    nombre_2 = models.CharField(max_length=30, null=True)
    apellido_1 = models.CharField(max_length=30, null=True)
    apellido_2 = models.CharField(max_length=30, null=True)
    nid = models.CharField(max_length=30)
    tipo_nid=models.CharField(max_length=30, choices=TIPO_NID)
    semestre = models.CharField(max_length=30 , choices=SEMESTRE_ESTUDIANTE, blank=True)
    genero = models.CharField(max_length=30, choices=GENERO_ESTUDIANTE, null=True)
    programa_academico = models.ForeignKey(Programa)
    correo = models.EmailField(max_length=30, unique=True)
    telefono = models.CharField(max_length=30, null=True)
    inscripcion = models.ManyToManyField(Inscripcion, null=True, blank=True)
    Estado = models.CharField(max_length=20, choices=ESTADOS_ESTUDIANTE, default='ACTIVO')
    ciclo_lectivo = models.CharField(max_length=30, null=True)

    def __unicode__(self):
        return unicode(self.Codigo_estudiante)


class InscripcionEstudiante(models.Model):
    actividad = models.ForeignKey(Programacion, null=True)
    estudiante = models.ForeignKey(Estudiantes)
    fecha_inscripcion = models.DateField(auto_now=True)

    def __unicode__(self):
        return unicode(self.actividad)