from django.contrib import admin
from .models import Servicio, TipoActividad, Actividad

# Register your models here.
class Servicios (admin.ModelAdmin):
	list_display = ['id','Codigo_servicio', 'nombre']
	class Meta:
		model = Servicio

class TipoActividade (admin.ModelAdmin):
	list_display = ['id','Codigo_tipoActividad', 'nombre']
	class Meta:
		model = TipoActividad


class Actividades (admin.ModelAdmin):
	list_display = ['id', 'servicio', 'tipo_actividad','Cupo_Actividad','Estado_actividad']
	class Meta:
		model = Actividad

admin.site.register(Servicio)
admin.site.register(TipoActividad)
admin.site.register(Actividad, Actividades)
