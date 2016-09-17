from django.db import models

class Profesor(models.Model):

    ESTADOS_PROFESOR = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )

    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    id_ucc = models.PositiveSmallIntegerField(primary_key=True)
    Identificacion = models.PositiveSmallIntegerField()
    Usuario = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, choices=ESTADOS_PROFESOR)

    def __unicode__(self):
        return unicode(self.nombres)
