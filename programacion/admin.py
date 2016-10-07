from django.contrib import admin
from .models import Programacion,Lugar,Horario,DiaActividad
# Register your models here.

class Horarios (admin.ModelAdmin):
	list_display = ['id','Hora_Inicio','Hora_Final']
	class Meta:
		model = Horario

class Lugares (admin.ModelAdmin):
	list_display = ['id','NombreLugar']
	class Meta:
		model = Lugar

class Dia_Semana (admin.ModelAdmin):
	list_display = ['id','Dia_Actividad','Horario']
	class Meta:
		model = DiaActividad

class Programaciones (admin.ModelAdmin):
	list_display = ['id','Servicio','actividad','profesor','lugarActividad','Fecha_Inicio','Fecha_Final']
	class Meta:
		model = Programacion



admin.site.register(Programacion, Programaciones)
admin.site.register(Lugar,Lugares)
admin.site.register(Horario,Horarios)
admin.site.register(DiaActividad,Dia_Semana)
