from django.shortcuts import render
from .models import Actividad
from django.shortcuts import get_object_or_404

def lista_actividades(request):

    a = Actividad.objects.all()

    return render(request, 'actividades/lista_actividades.html', {'a':a})


def detalle_actividad(request, id_actividad):

    b = get_object_or_404(Actividad, pk=id_actividad)

    return render(request, 'actividades/detalle_actividad.html', {'b':b})
