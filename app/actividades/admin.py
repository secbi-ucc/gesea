from django.contrib import admin
from .models import Servicio, Actividad, RegistroActividad

# Register your models here.
class Actividades (admin.ModelAdmin):
	list_display = ['tipo_actividad','Cupo_Actividad', 'Estado_actividad']
	list_editable = ['Estado_actividad',]
	list_filter = ['tipo_actividad', 'Estado_actividad']

	class Meta:
		model = Actividad



class ThingInline(admin.TabularInline):
	model = RegistroActividad
	min_num = 0
	extra = 0
	raw_id_fields = ('servicio',)
	verbose_name_plural = 'Reg Actividades'
	suit_form_inlines_hide_original = True

class Servicios (admin.ModelAdmin):
	list_display = ['id','Codigo_servicio', 'nombre']
	inlines = [
			ThingInline,
		]

	class Meta:
		model = Servicio

class registroactividad (admin.ModelAdmin):
	list_display = ['servicio','actividad']
	raw_id_fields = ('servicio','actividad')
	class Meta:
		model = RegistroActividad


admin.site.register(Servicio, Servicios)
admin.site.register(RegistroActividad, registroactividad)
admin.site.register(Actividad, Actividades)
