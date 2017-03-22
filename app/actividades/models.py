from django.db import models
#Modelo de la clase servicio
class Servicio(models.Model):
    NOMBRES_SERVICIOS = (
        ('PROMOCION DE LA SALUD', 'Promocion de la salud'),
        ('DEPORTES', 'Deportes'),
        ('PATRIMONIO CULTURAL', 'Patrimonio cultural'),
        ('ORIENTACION Y ACOMPANAMIENTO', 'Orientacion y acompanamiento'),
    )
    Codigo_servicio = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=50, choices=NOMBRES_SERVICIOS)

    def __unicode__(self):
        return unicode(self.nombre)

#Modelo de la clase tipo de actividad
class TipoActividad(models.Model):
    TIPOS_ACTIVIDADES = (
        ('ATENCION PSICOLOGICA', 'Atencion psicologica'),
        ('ATENCION PSICOSOCIAL', 'Atencion psicosocial '),
        ('CONSEJERIAS', 'Consejerias'),
        ('DANZA', 'Danza'),
        ('FUTBOL 11', 'Futbol 11'),
        ('GESTION AMBIENTAL', 'Gestion ambiental'),
        ('MEDICINA GENERAL', 'Medicina general'),
        ('MICROFUTBOL', 'Microfutbol Masc Y Fem'),
        ('MUSICA', 'Musica'),
        ('ORIENTACION ESPIRITUAL-CONVIVENCIA', 'Orientacion espiritual- convivencia'),
        ('PRIMEROS AUXILIOS', 'Primeros auxilios'),
        ('PROMOCIONES SOCIOECONOMICAS', 'promociones socioeconomicas'),
        ('SOFTBOL', 'Softbol'),
        ('TEATRO', 'Teatro'),
        ('TORNEO EMPRESARIAL MINIFUTBOL', 'Torneo Empresarial Mini Futbol'),
        ('TORNEO INTERNO MICRO', 'Torneo Interno Micro'),
        ('VOLEIBOL', 'Voleibol Masc Y Fem'),
    )

    Codigo_tipoActividad = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=50, choices=TIPOS_ACTIVIDADES)
    class Meta:
        verbose_name_plural = "Tipo Actividad"

    def __unicode__(self):
        return unicode(self.nombre)

#Modelo de la clase actividad
class Actividad(models.Model):
    ESTADOS_ACTIVIDAD = (
        ('ABIERTA', 'Abierta'),
        ('CERRADA', 'Cerrada'),
    )
    servicio =  models.ForeignKey(Servicio)
    Codigo_actividad = models.CharField(max_length=10,unique=True)
    tipo_actividad = models.ForeignKey(TipoActividad)
    Estado_actividad =  models.CharField(max_length=30, choices=ESTADOS_ACTIVIDAD, default='ABIERTA')
    Cupo_Actividad = models.IntegerField(max_length = 5)
    class Meta:
        verbose_name_plural = "Actividad"
    def __unicode__(self):
        return unicode(self.tipo_actividad)
