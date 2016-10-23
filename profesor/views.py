from django.shortcuts import render
from .models import Profesor
# Create your views here.

def agregar_prof (request):

        return render (request, 'profesor/agregar_profesor.html',)


def profesor_forms(request):

            return render(request, 'profesor/forms/profesoresf.html',)
