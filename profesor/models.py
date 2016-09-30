from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):

    ESTADOS_PROFESOR = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    user = models.OneToOneField(User)
    Nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    id_ucc = models.PositiveSmallIntegerField(primary_key=True)
    Identificacion = models.PositiveSmallIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS_PROFESOR)

    def __unicode__(self):
        return unicode(self.Nombre)
