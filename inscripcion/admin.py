from django.contrib import admin
from .models import Estudiantes , Inscripcion


# Register your models here.

class Estudiante (admin.ModelAdmin):
	list_display = ['idEstudiante','nombre','apellidos','semestre','sexo','facultad','correo','telefono']
	class Meta:
		model = Estudiantes

class Inscripciones (admin.ModelAdmin):
	list_display = ['id','TipodeParticipacion','estudiante']
	class Meta:
		model = Inscripcion

admin.site.register(Estudiantes,Estudiante)
admin.site.register(Inscripcion,Inscripciones)
