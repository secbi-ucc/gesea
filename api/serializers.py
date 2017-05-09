# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from inscripcion.models import AsistenciaEstudiante, Estudiantes, Instructor
from programacion.models import Programacion, DiaActividad, Horario
from actividades.models import Actividad
from rest_framework import serializers
from django.contrib.auth.models import User



class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actividad
        fields = ('Codigo_actividad', 'tipo_actividad', 'Estado_actividad', 'Cupo_Actividad')
        read_only_fields = ('Codigo_actividad', 'tipo_actividad', 'Estado_actividad', 'Cupo_Actividad')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('get_full_name', 'email', 'username')
        read_only_fields = ('get_full_name', 'email', 'username')

class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ('Hora_Inicio', 'Hora_Final', 'get_time_diff' )


class DiaActividadSerializer(serializers.HyperlinkedModelSerializer):
    Horario =  HorarioSerializer(read_only=True)
    class Meta:
        model = DiaActividad
        fields = ('Dia_Actividad', 'Horario' )



class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instructor
        fields = ('id_ucc', 'nombre_completo')

class ProgramacionSerializer(serializers.HyperlinkedModelSerializer):
    #Instructor = InstructorSerializer(read_only=True)
    Dia_semana = DiaActividadSerializer(read_only=True, many=True)
    actividad = ActividadSerializer(read_only=True)

    class Meta:
        model = Programacion
        fields = ('id', 'actividad' , 'Dia_semana')

class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estudiantes
        fields = ('ID_Estudiante', 'nombre_completo')



class AsistenciaEstudianteSerializer(serializers.HyperlinkedModelSerializer):
    #programacion = ProgramacionSerializer(read_only=True)
    estudiante = EstudianteSerializer(read_only=True)

    class Meta:
        model = AsistenciaEstudiante
        fields = ('url', 'id', 'estudiante','fecha_asistencia' , 'n_horas',)
        read_only_fields = ('fecha_asistencia',)