from django.contrib import admin
from .models import Programacion,Lugar,Horario,DiaActividad
from inscripcion.models import Inscripcion
# Register your models here.

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

class Programaciones (admin.ModelAdmin):

	def estudiantes_inscritos(self, obj):
		return '<a  href="/admin/inscripcion/inscripcion/?programacion__id=%d" class="link"><i class="icon-list"></i></a>' % obj.id
	estudiantes_inscritos.short_description = 'Lista inscritos'
	estudiantes_inscritos.allow_tags = True
	def n_estudiantes_inscritos(self, obj):
		return '%d' % Inscripcion.objects.filter(programacion=obj.id).count()
		n_estudiantes_inscritos.short_description = 'Numero de inscritos'
		n_estudiantes_inscritos.allow_tags = True
	list_display = ['actividad','profesor','lugarActividad','horario','estudiantes_inscritos','n_estudiantes_inscritos']
	inlines = [
		ThingInline,
	]
	class Meta:
		model = Programacion




admin.site.register(Lugar,Lugares)
admin.site.register(Horario,Horarios)
admin.site.register(DiaActividad,Dia_Semana)
admin.site.register(Programacion, Programaciones)
