from django.contrib import admin
from .models import Programacion,Lugar,Horario,DiaActividad
from inscripcion.models import Inscripcion

class Horarios (admin.ModelAdmin):
	list_display = ['Hora_Inicio','Hora_Final']
	class Meta:
		model = Horario

class Lugares (admin.ModelAdmin):
	list_display = ['NombreLugar']
	class Meta:
		model = Lugar

class Dia_Semana (admin.ModelAdmin):
	list_display = ['Dia_Actividad','Horario']
	class Meta:
		model = DiaActividad

class ThingInline(admin.TabularInline):
	model = Inscripcion
	min_num = 0
	extra = 0
	raw_id_fields = ('estudiante',)
	verbose_name_plural = 'Estudiantes Inscritos'
	suit_form_inlines_hide_original = True

class Programaciones (admin.ModelAdmin):

	def estudiantes_inscritos(self, obj):
		return '<a  href="/admin/inscripcion/inscripcion/?programacion__id=%d" class="link">Lista</a>' % obj.id
	estudiantes_inscritos.short_description = 'Lista inscritos'
	estudiantes_inscritos.allow_tags = True
	def n_estudiantes_inscritos(self, obj):
		return '%d' % Inscripcion.objects.filter(programacion=obj.id).count()
		n_estudiantes_inscritos.short_description = 'Numero de inscritos'
		n_estudiantes_inscritos.allow_tags = True

	def reporte_actividad(self, instance):
		return "<a href='/admin/reporte/actividad/%s'> <i style='font-size:17px' class='fa fa-file-pdf-o' aria-hidden='true'></i>  </a>" % instance.id

	reporte_actividad.short_description = "Reporte"
	reporte_actividad.allow_tags = True
	reporte_actividad.is_column = True

	list_display = ['actividad','lugarActividad','horario','estudiantes_inscritos','n_estudiantes_inscritos','reporte_actividad']
	list_filter = ['actividad' ]
	inlines = [
		ThingInline,
	]
	class Meta:
		model = Programacion




admin.site.register(Lugar,Lugares)
admin.site.register(Horario,Horarios)
admin.site.register(DiaActividad,Dia_Semana)
admin.site.register(Programacion, Programaciones)
