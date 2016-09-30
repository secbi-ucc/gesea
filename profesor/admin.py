from django.contrib import admin
from .models import Profesor


class Profesores (admin.ModelAdmin):
	list_display = ['id_ucc','Nombre','apellidos','Identificacion','estado']
	class Meta:
		model = Profesor

admin.site.register(Profesor,Profesores)
# Register your models here.
