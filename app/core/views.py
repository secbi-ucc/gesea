from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
from inscripcion.models import Inscripcion, Estudiantes
from programacion.models import Programacion
from profesor.models import Profesor
from inscripcion.models import AsistenciaEstudiante
from django.utils.timezone import now
from django.views.decorators.http import require_POST

def inicio(request):


    return render(request, 'core/inicio.html', {})

@login_required ()
def no_permitido(request):


    return render(request, 'core/no_permitido.html', {})


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


@staff_member_required
def listado_asistencia(request, is_refresh=None):


    user = request.user
    pr = Profesor.objects.get(user = user)
    a = None
    p = Programacion.objects.filter(profesor=pr).last()
    i = Inscripcion.objects.filter(programacion=p)

    show_list = False

    if request.POST.get("tomar_lista", "") or is_refresh == '1':
        show_list = True
        e = Estudiantes.objects.filter(ID_Estudiante__in=list(Inscripcion.objects.filter(programacion=p).values_list('estudiante', flat=True)))

        a = AsistenciaEstudiante.objects.filter(programacion=p, fecha_asistencia=now())

        if not a:

            for i in range(len(e)):
                AsistenciaEstudiante(programacion=p, estudiante=e[i]).save()

        a = AsistenciaEstudiante.objects.filter(programacion = p)



    context = admin.site.each_context(request)
    context.update({
        'title': 'Lista asistencia',
        'i': i,
        'p': p,
        'a': a,
        'show_list': show_list,
    })

    template = 'core/lista_asistencia.html'
    return render(request, template, context)