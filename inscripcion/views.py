from django.shortcuts import render
from .models import Estudiantes, Inscripcion
from django.shortcuts import get_object_or_404

# Create your views here.

def inscripcion_lis (request):

    return render(request, 'inscripcion/inscripcion_nueva.html',)

def inscripcion_forms(request):

    return render(request, 'inscripcion/forms/inscripcionesf.html',)

def estudianteslis(request):

    return render(request, 'inscripcion/lista_estudiantes.html',)

def agregar_usuario(request):

    return render (request, 'inscripcion/forms/agregar_usuario.html',)
