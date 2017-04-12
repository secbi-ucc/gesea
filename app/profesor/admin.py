from django.contrib import admin
from .models import Instructor

class Instructores (admin.ModelAdmin):
	list_display = ['id_ucc','user','Identificacion','Nombre','Primer_Apellido','Segundo_Apellido','estado']
	class Meta:
		model = Instructor

admin.site.register(Instructor,Instructores)

# Register your models here.
