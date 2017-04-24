from django import template
from programacion.models import Programacion
from inscripcion.models import Estudiantes, AsistenciaEstudiante


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
