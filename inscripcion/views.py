from django.shortcuts import render
from .models import Estudiantes, Inscripcion
from django.shortcuts import get_object_or_404


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
@login_required ( login_url = '/login/' )
def inscripcion_lis (request):
    a = Estudiantes.objects.all()
    return render(request, 'inscripcion/inscripcion_nueva.html', {'a':a})
@login_required ( login_url = '/login/' )
def inscripcion_forms(request):

    return render(request, 'inscripcion/forms/inscripcionesf.html',)
@login_required ( login_url = '/login/' )
def estudianteslis(request):
    estudiantes = Estudiantes.objects.all()
    paginator = Paginator(estudiantes, 25)
    page = request.GET.get('page')
    try:
        a = paginator.page(page)
    except PageNotAnInteger:
        a = paginator.page(1)
    except EmptyPage:
        a = paginator.page(paginator.num_pages)

    return render(request, 'inscripcion/lista_estudiantes.html', {'a':a})
@login_required ( login_url = '/login/' )
def agregar_usuario(request):

    return render (request, 'inscripcion/forms/agregar_usuario.html',)
@login_required ( login_url = '/login/' )
def detalle_estudiante(request, id_estudiante):

    b = get_object_or_404(Estudiantes, pk=id_estudiante)

    return render(request, 'inscripcion/detalle_estudiante.html', {'b':b})


@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def editar_estudiante(request, id_estudiante):
    instance = get_object_or_404(Estudiantes, pk=id_estudiante)
    a = instance
    form = EstudiantesForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            a = Estudiantes.objects.all()
            b = "Estudiante Actualizado Correctamente"
            return render(request, 'inscripcion/lista_estudiantes.html', {'a': a,'b':b})
    return render(request, 'inscripcion/editar_estudiante.html', {'form': form,'a':a})
