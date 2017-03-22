from __future__ import unicode_literals
from django.db import models
from programacion.models import Programacion
from actividades.models import Actividad


# Create your models here.

class Programa(models.Model):
    cod = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Programas"

    def __unicode__(self):
        return unicode(self.nombre)


class Estudiantes(models.Model):
    GENERO_ESTUDIANTE = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    TIPO_NID = (
        ('TI', 'TI'),
        ('CC', 'CC'),
    )

    class Meta:
        verbose_name_plural = "Estudiantes"

    ID_Estudiante = models.CharField(max_length=10, primary_key=True)
    Primer_Nombre= models.CharField(max_length=30, null=True)
    Segundo_Nombre = models.CharField(max_length=30, null=True)
    Primer_Apellido = models.CharField(max_length=30, null=True)
    Segundo_Apellido= models.CharField(max_length=30, null=True)
    Nro_Documento = models.CharField(max_length=30)
    Tipo_Documento=models.CharField(max_length=30, choices=TIPO_NID)
    genero = models.CharField(max_length=30, choices=GENERO_ESTUDIANTE, null=True)
    Programa_Academico = models.ForeignKey(Programa, null=True)
    Correo_Institucional = models.EmailField(max_length=50, unique=True)
    Nro_Telefonico = models.CharField(max_length=30, null=True)
    Ciclo_Lectivo = models.CharField(max_length=30, null=True)
    Descripcion = models.CharField(max_length=30, null=True)


    def __unicode__(self):
        return unicode(self.ID_Estudiante)



class Inscripcion(models.Model):
    programacion = models.ForeignKey(Programacion, null=True)
    estudiante = models.ForeignKey(Estudiantes, null=True)
    fecha_inscripcion = models.DateField(auto_now=True, null=True)

    def __unicode__(self):
        return unicode(self.programacion)
