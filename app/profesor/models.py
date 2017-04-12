from django.db import models
from django.contrib.auth.models import User

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

    def __unicode__(self):
        return unicode(self.Nombre)
