#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Estudiantes, Inscripcion, Programa
from import_export import resources
#
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class EstudianteResource(resources.ModelResource):

	Programa_Academico = fields.Field(attribute='Programa_Academico',
								   widget=ForeignKeyWidget(Programa, 'nombre'))

	class Meta:
		import_id_fields = ('ID_Estudiante',)
		model = Estudiantes
		export_order = ('Ciclo_Lectivo', 'Programa_Academico','ID_Estudiante','Tipo_Documento','Nro_Documento', 'Primer_Apellido', 'Segundo_Apellido', 'Primer_Nombre', 'Segundo_Nombre', 'Nro_Telefonico', 'Correo_Institucional','Descripcion')
		fields = ('Ciclo_Lectivo', 'Programa_Academico','ID_Estudiante','Tipo_Documento','Nro_Documento', 'Primer_Apellido', 'Segundo_Apellido', 'Primer_Nombre', 'Segundo_Nombre', 'Nro_Telefonico', 'Correo_Institucional','Descripcion')

class EstudianteAdmin(ImportExportModelAdmin):
    search_fields = ('Primer_Apellido', 'Segundo_Apellido',"Nro_Documento",)
    list_filter = ('Primer_Apellido',)
    list_display = ['Ciclo_Lectivo', 'Programa_Academico','ID_Estudiante','Tipo_Documento','Nro_Documento', 'Primer_Apellido', 'Segundo_Apellido', 'Primer_Nombre', 'Segundo_Nombre', 'Nro_Telefonico', 'Correo_Institucional','Descripcion']
    resource_class = EstudianteResource



class Inscripciones (admin.ModelAdmin):

	list_display = ['id','actividad']
	class Meta:
		model = Inscripcion

class Estudiante (admin.ModelAdmin):

	class Meta:
		model = Estudiantes


admin.site.register(Inscripcion, Inscripciones)
admin.site.register(Estudiantes, EstudianteAdmin)
admin.site.register(Programa)
