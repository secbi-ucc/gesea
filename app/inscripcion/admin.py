#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Estudiantes, Programa, Inscripcion, AsistenciaEstudiante
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
    search_fields = ('Primer_Apellido', 'Segundo_Apellido','Nro_Documento','Primer_Nombre', 'Segundo_Nombre', 'ID_Estudiante')
    list_filter = ('Ciclo_Lectivo','Programa_Academico')
    list_display = ['ID_Estudiante', 'Programa_Academico','Nro_Documento', 'Primer_Apellido', 'Segundo_Apellido', 'Primer_Nombre', 'Segundo_Nombre', 'Nro_Telefonico']
    resource_class = EstudianteResource




class Inscripciones (admin.ModelAdmin):
    search_fields = ('estudiante__Primer_Nombre',)
    list_filter = ('programacion', 'fecha_inscripcion' )
    list_display = ['fecha_inscripcion','programacion', 'nombre_completo', 'id_ucc']
    raw_id_fields = ('estudiante', 'programacion' )

    def nombre_completo(self, obj):
     return obj.estudiante.Primer_Nombre + " " + obj.estudiante.Segundo_Nombre + " " + obj.estudiante.Primer_Apellido + " " + obj.estudiante.Segundo_Apellido

    def id_ucc(self, obj):
     return obj.estudiante.ID_Estudiante


class AsistenciaEstudianteAdmin (admin.ModelAdmin):
    search_fields = ('estudiante__Primer_Nombre',)
    list_filter = ('programacion', 'fecha_asistencia' )
    list_display = ['fecha_asistencia','programacion', 'nombre_completo', 'id_ucc']
    readonly_fields = ('fecha_asistencia', 'asistio' )

    def nombre_completo(self, obj):
     return obj.estudiante.Primer_Nombre + " " + obj.estudiante.Segundo_Nombre + " " + obj.estudiante.Primer_Apellido + " " + obj.estudiante.Segundo_Apellido

    def id_ucc(self, obj):
     return obj.estudiante.ID_Estudiante



admin.site.register(Inscripcion, Inscripciones)
admin.site.register(Estudiantes, EstudianteAdmin)
admin.site.register(Programa)
admin.site.register(AsistenciaEstudiante, AsistenciaEstudianteAdmin)
