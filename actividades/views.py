from django.shortcuts import render
from .models import Actividad
from django.shortcuts import get_object_or_404
from .forms import ActividadForm
from django.contrib.auth.decorators import login_required


@login_required ( login_url = '/login/' )
def lista_actividades(request):

    a = Actividad.objects.all()


    return render(request, 'actividades/lista_actividades.html', {'a':a})

@login_required ( login_url = '/login/' )
def detalle_actividad(request, id_actividad):

    b = get_object_or_404(Actividad, pk=id_actividad)

    return render(request, 'actividades/detalle_actividad.html', {'b':b})

@login_required ( login_url = '/login/' )
def nueva_actividad(request):

    form_actividad = ActividadForm()

    if request.method == "POST":
        form_actividad = ActividadForm(request.POST)

        if form_actividad.is_valid():
            form_actividad.save()
            return render(request, "actividades/nueva_actividad_mesaje.html")

    return render(request,"actividades/nueva_actividad_form.html", {"form_actividad":form_actividad})
