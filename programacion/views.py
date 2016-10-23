from django.shortcuts import render
from .models import Programacion,Lugar,Horario
from django.shortcuts import get_object_or_404
#from .forms import ActividadForm

# Create your views here.

def horario_form(request):

    h = Programacion.objects.all()

    return render(request, 'programacion/forms/horario.html', {'h':h})

def horario_actividad(request):

    i = Programacion.objects.all()

    return render(request, 'programacion/horario_actividad.html', {'i':i})

def lugar_actividad(request):

    j = Programacion.objects.all()

    return render(request, 'programacion/lugar_actividad.html', {'j':j})

def lugar_form(request):

    k = Programacion.objects.all()

    return render(request, 'programacion/forms/lugar.html', {'k':k})

def programacion_actividad(request):

    l = Programacion.objects.all()

    return render(request, 'programacion/programacion.html', {'l':l})

def dia_actividad(request):

    m = Programacion.objects.all()

    return render(request, 'programacion/dia_actividad.html', {'m':m})

def dia_form(request):

    n = Programacion.objects.all()

    return render(request, 'programacion/forms/dia.html', {'n':n})

def programacion_form(request):

    o = Programacion.objects.all()

    return render(request, 'programacion/forms/programacion.html', {'o':o})
