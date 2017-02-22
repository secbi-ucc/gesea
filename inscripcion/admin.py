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

	programa_academico = fields.Field(attribute='programa_academico',
								   widget=ForeignKeyWidget(Programa, 'nombre'))

	class Meta:
		import_id_fields = ('Codigo_estudiante',)
		model = Estudiantes
		export_order = ('Codigo_estudiante', 'programa_academico', 'apellido_1', 'apellido_2', 'nombre_1', 'nombre_2', 'telefono', 'correo')
		fields = ('Codigo_estudiante', 'programa_academico', 'apellido_1', 'apellido_2', 'nombre_1', 'nombre_2', 'telefono', 'correo')

class EstudianteAdmin(ImportExportModelAdmin):
    search_fields = ('apellido_1',)
    list_filter = ('programa_academico',)
    list_display = ['Codigo_estudiante', 'nombre_1', 'apellido_1', 'programa_academico', 'genero', 'correo', 'telefono']
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
