from django.contrib import admin
from .models import Estudiantes, Inscripcion


# Register your models here.

class Inscripciones (admin.ModelAdmin):
	list_display = ['id','TipodeParticipacion']
	class Meta:
		model = Inscripcion

class Estudiante (admin.ModelAdmin):
	list_display = ['idEstudiante','Horas_estudiante','nombre','apellidos','semestre','sexo','facultad','correo','telefono']
	class Meta:
		model = Estudiantes

admin.site.register(Inscripcion,Inscripciones)
admin.site.register(Estudiantes,Estudiante)
