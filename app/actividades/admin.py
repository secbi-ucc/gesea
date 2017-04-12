from django.contrib import admin
from .models import Area, Actividad, RegistroActividad

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
	raw_id_fields = ('area',)
	verbose_name_plural = 'Reg Actividades'
	suit_form_inlines_hide_original = True

class Areas (admin.ModelAdmin):
	list_display = ['id','Codigo_area', 'nombre']
	inlines = [
			ThingInline,
		]

	class Meta:
		model = Area

class registroactividad (admin.ModelAdmin):
	list_display = ['area','actividad']
	raw_id_fields = ('area','actividad')
	class Meta:
		model = RegistroActividad


admin.site.register(Area, Areas)
admin.site.register(RegistroActividad, registroactividad)
admin.site.register(Actividad, Actividades)
