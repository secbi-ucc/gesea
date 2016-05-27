from django.db import models
from profesor.models import Profesor
from actividades.models import Actividad

class Programacion(models.Model):
    profesor = models.ForeignKey(Profesor)
    programacion_actividad = models.ForeignKey(Actividad)
