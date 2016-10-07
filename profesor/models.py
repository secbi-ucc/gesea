from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):

    ESTADOS_PROFESOR = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )
    user = models.OneToOneField(User)
    id_ucc = models.PositiveSmallIntegerField(primary_key=True)
    Identificacion = models.PositiveSmallIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS_PROFESOR, default='ACTIVO')

    def __unicode__(self):
        return unicode(self.user)
