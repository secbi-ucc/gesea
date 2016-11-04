from django.shortcuts import render
from .models import Estudiantes, Inscripcion
from django.shortcuts import get_object_or_404
from .forms import EstudiantesForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def inscripcion_lis (request):
    a = Estudiantes.objects.all()
    return render(request, 'inscripcion/inscripcion_nueva.html', {'a':a})

def inscripcion_forms(request):

    return render(request, 'inscripcion/forms/inscripcionesf.html',)

def estudianteslis(request):
    a = Estudiantes.objects.all()

    return render(request, 'inscripcion/lista_estudiantes.html', {'a':a})

def agregar_usuario(request):

    return render (request, 'inscripcion/forms/agregar_usuario.html',)
def detalle_estudiante(request, id_Estudiantes):

    b = get_object_or_404(Estudiantes, pk=id_Estudiantes)

    return render(request, 'inscripcion/detalle_estudiante.html', {'b':b})

def agregar_estudiante(request):

    form_estudiante = EstudiantesForm()

    if request.method == "POST":
        form_estudiante = EstudiantesForm(request.POST)

        if form_estudiante.is_valid():
            form_estudiante.save()
            return render(request, "inscripcion/agregar_estudiante_mensaje.html")

    return render(request,"inscripcion/agregar_estudiante_form.html", {"form_estudiante":form_estudiante})

def editar_estudiante(request, id_Estudiantes):
    instance = get_object_or_404(Estudiantes, pk=id_Estudiantes)
    a = instance
    form = EstudiantesForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            a = Estudiantes.objects.all()
            b = "Estudiante Actualizado Correctamente"
            return render(request, 'inscripcion/lista_estudiantes.html', {'a': a,'b':b})
    return render(request, 'inscripcion/editar_estudiante.html', {'form': form,'a':a})
