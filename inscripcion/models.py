from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Estudiantes(models.Model):
    idEstudiante = models.AutoField( primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    semestre = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30)
    facultad = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.nombre)

class Inscripcion(models.Model):
    Tipo_participacion = (
        ('Curso', 'Curso'),
        ('Grupo de representacion', 'Grupo de representacion'),
        ('Equipos de representacion', 'Equipos de representacion'),
        ('Brigada', 'Brigada'),
        ('Otro', 'Otro'),
    )
    TipodeParticipacion = models.CharField(max_length=30, choices=Tipo_participacion)
    estudiante = models.ForeignKey(Estudiantes)
    def __unicode__(self):
        return unicode(self.TipodeParticipacion)
