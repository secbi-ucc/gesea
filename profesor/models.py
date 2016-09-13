from django.db import models

class Profesor(models.Model):

    ESTADOS_PROFESOR = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )

    nombres = models.CharField(max_length=30)
    id_ucc = models.PositiveSmallIntegerField(primary_key=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_PROFESOR)

    def __unicode__(self):
        return unicode(self.nombres)
