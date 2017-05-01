from __future__ import unicode_literals
from django.db import models
from programacion.models import Programacion
from actividades.models import Actividad
from django.utils.timezone import now
from django.contrib.auth.models import User


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
    foto_url = models.URLField(null=True)
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

    def nombre_completo(self):
        return self.Primer_Nombre + " " + self.Segundo_Nombre + " " + self.Primer_Apellido + " " + self.Segundo_Apellido



    def __unicode__(self):
        return unicode(self.Primer_Nombre)



class Inscripcion(models.Model):
    programacion = models.ForeignKey(Programacion, null=True)
    estudiante = models.ForeignKey(Estudiantes, null=True)
    fecha_inscripcion = models.DateField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "Estudiantes Inscritos"
        verbose_name = "Inscripcion individual"
    def __unicode__(self):
        return unicode(self.programacion)


class AsistenciaEstudiante(models.Model):

    programacion = models.ForeignKey(Programacion)
    estudiante = models.ForeignKey(Estudiantes)
    fecha_asistencia = models.DateField(default=now)
    asistio = models.NullBooleanField(null=True, default=False)
    n_horas = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Hisorial de asistencia"
        verbose_name = "Historia Asistencia"
    def __unicode__(self):
        return unicode(self.estudiante)

class Instructor(models.Model):

    ESTADOS_INSTRUCTOR = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    user = models.OneToOneField(User)
    id_ucc = models.IntegerField(primary_key=True)
    Identificacion = models.IntegerField(unique=True)
    Nombre = models.CharField(max_length=30)
    Primer_Apellido = models.CharField(max_length=20)
    Segundo_Apellido = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, choices=ESTADOS_INSTRUCTOR, default='ACTIVO')
    class Meta:
        verbose_name_plural = "Instructores"

    def nombre_completo(self):
        return self.Nombre + " " + self.Primer_Apellido + " " + self.Segundo_Apellido

    def __unicode__(self):
        return unicode(self.Nombre)