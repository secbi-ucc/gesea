from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):

    ESTADOS_PROFESOR = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    user = models.OneToOneField(User)
    id_ucc = models.IntegerField(primary_key=True)
    Identificacion = models.IntegerField(unique=True)
    Nombre = models.CharField(max_length=30)
    Primer_Apellido = models.CharField(max_length=20)
    Segundo_Apellido = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, choices=ESTADOS_PROFESOR, default='ACTIVO')
    class Meta:
        verbose_name_plural = "Profesores"

    def __unicode__(self):
        return unicode(self.Nombre)
