from django.contrib import admin
from .models import Programacion,Lugar,Horario
# Register your models here.

class Horarios (admin.ModelAdmin):
	list_display = ['id','Fecha_Inicio','Fecha_Final']
	class Meta:
		model = Horario

class Programaciones (admin.ModelAdmin):
	list_display = ['id','Servicio','actividad','inscripcion','profesor','lugarActividad','horario']
	class Meta:
		model = Programacion

class Lugares (admin.ModelAdmin):
	list_display = ['id','NombreLugar']
	class Meta:
		model = Lugar

admin.site.register(Programacion, Programaciones)
admin.site.register(Lugar,Lugares)
admin.site.register(Horario,Horarios)
