from django import template
from django.shortcuts import render, redirect, get_object_or_404
from inscripcion.models import Estudiantes, AsistenciaEstudiante, Inscripcion
from programacion.models import Programacion



register = template.Library()

@register.simple_tag
def total_horas_programacion(p_id, e_id):
    total_a = 0

    p = Programacion.objects.get(id=p_id)
    e = Estudiantes.objects.get(ID_Estudiante=e_id)
    p_e_a = AsistenciaEstudiante.objects.filter(programacion=p, estudiante=e)

    for a in p_e_a:
        total_a = total_a + a.n_horas

    return total_a

@register.simple_tag
def total_horas_estudiante(e_id):
    total_a = 0

    e = Estudiantes.objects.get(ID_Estudiante=e_id)
    p_e_a = AsistenciaEstudiante.objects.filter(estudiante=e)

    for a in p_e_a:
        total_a = total_a + a.n_horas

    return total_a

@register.simple_tag
def total_num_estudiante(a_id):
    total_a = 0
    progra = get_object_or_404(Programacion, id=a_id)
    inscritos = Inscripcion.objects.filter(programacion=progra)


    for estu in inscritos:
        total_a = total_a + 1

    return total_a



