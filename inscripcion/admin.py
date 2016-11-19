from django.contrib import admin
from .models import Estudiantes, Inscripcion


# Register your models here.

class Inscripciones (admin.ModelAdmin):
	list_display = ['id','actividad']
	class Meta:
		model = Inscripcion

class Estudiante (admin.ModelAdmin):
	list_display = ['Codigo_estudiante','Horas_estudiante','nombre','apellidos','semestre','sexo','facultad','correo','Estado','telefono']
	class Meta:
		model = Estudiantes

admin.site.register(Inscripcion,Inscripciones)
admin.site.register(Estudiantes,Estudiante)
