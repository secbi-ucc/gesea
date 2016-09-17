from django.contrib import admin
from .models import Servicio, TipoActividad, Actividad

# Register your models here.


class Actividades (admin.ModelAdmin):
	list_display = ['id', 'servicio', 'tipo_actividad','Cupo_Actividad','Numero_Estudiantes','Estado_actividad']
	class Meta:
		model = Actividad

admin.site.register(Servicio)
admin.site.register(TipoActividad)
admin.site.register(Actividad, Actividades)
