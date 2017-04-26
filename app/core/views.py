from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
from inscripcion.models import Inscripcion, Estudiantes
from programacion.models import Programacion, Horario
from inscripcion.models import Instructor
from inscripcion.models import AsistenciaEstudiante
from programacion.models import Actividad
from django.utils.timezone import now
from django.views.decorators.http import require_POST

def inicio(request):


    return render(request, 'core/inicio.html', {})

@login_required ()
def no_permitido(request):


    return render(request, 'core/no_permitido.html', {})

@login_required ()
def reporte_asistencia_estudiantes(request, id_estudiante):

    e = get_object_or_404(Estudiantes, ID_Estudiante=id_estudiante)
    a = AsistenciaEstudiante.objects.filter(estudiante=e)


    context = admin.site.each_context(request)
    context.update({
        'a': a,
        'e': e
    })
    return render(request, 'core/reporte_asistencia_estudiante.html', context)

@login_required ()
def reporte_estudiantes_inscritos(request, id):
    progra= get_object_or_404(Programacion,id=id)
    inscritos = Inscripcion.objects.filter(programacion=progra)
    context = admin.site.each_context(request)
    context.update({
        'progra': progra,
        'inscritos': inscritos
    })
    return render(request, 'core/reporte_estudiantes_actividades.html',context)

@require_POST
def flag_asistio(request, asistencia_id):
    p = AsistenciaEstudiante.objects.get(id=asistencia_id)
    p.asistio = True
    p.save()
    return redirect("/admin/asistencia/1")
@require_POST
def flag_no_asistio(request, asistencia_id):
    p = AsistenciaEstudiante.objects.get(id=asistencia_id)
    p.asistio = False
    p.save()
    return redirect("/admin/asistencia/1")


@require_POST
def agregar_horas_asistencia(request, programacion_id, asistencia_id):
    a = AsistenciaEstudiante.objects.get(id=asistencia_id)
    p = Programacion.objects.get(id=programacion_id)

    print get_day_hours(p).get_time_diff()

    horas_to_add = request.POST.get("n_horas", "")

    a.n_horas = horas_to_add
    a.save()
    return redirect("/admin/asistencia/1")


@staff_member_required
def listado_asistencia(request, is_refresh=None):


    user = request.user
    pr = Instructor.objects.get(user = user)
    a = None
    p = Programacion.objects.filter(Instructor=pr).last()
    h = get_day_hours(p)
    i = Inscripcion.objects.filter(programacion=p)

    show_list = False

    if request.POST.get("tomar_lista", "") or is_refresh == '1':
        show_list = True
        e = Estudiantes.objects.filter(ID_Estudiante__in=list(Inscripcion.objects.filter(programacion=p).values_list('estudiante', flat=True)))

        a = AsistenciaEstudiante.objects.filter(programacion=p, fecha_asistencia=now())

        if not a:

            for i in range(len(e)):
                AsistenciaEstudiante(programacion=p, estudiante=e[i]).save()

        a = AsistenciaEstudiante.objects.filter(programacion = p, fecha_asistencia=now())



    context = admin.site.each_context(request)
    context.update({
        'title': 'Lista asistencia',
        'i': i,
        'p': p,
        'a': a,
        'h': h,
        'show_list': show_list,
    })

    template = 'core/lista_asistencia.html'
    return render(request, template, context)


def get_day_hours(p):

    print get_current_day_name()

    current_day_horario = p.Dia_semana.filter(Dia_Actividad=get_current_day_name()).values('Horario__id')


    print current_day_horario

    horario_id =  current_day_horario[0]['Horario__id']

    h = Horario.objects.get(id=horario_id)

    return h


def get_current_day_name():

    current_day = None

    if now().strftime("%w") == '2':
        current_day = 'LUNES'
    elif now().strftime("%w") == '3':
        current_day = 'MARTES'
    elif now().strftime("%w") == '4':
        current_day = 'MIERCOLES'
    elif now().strftime("%w") == '5':
        current_day = 'JUEVES'
    elif now().strftime("%w") == '6':
        current_day = 'VIERNES'
    elif now().strftime("%w") == '7':
        current_day = 'SABADO'
    elif now().strftime("%w") == '1':
        current_day = 'DOMINGO'

    print now().strftime("%w")

    return current_day