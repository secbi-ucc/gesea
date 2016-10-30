from django.shortcuts import render
from .models import Actividad
from .models import Servicio
from .models import TipoActividad
from django.shortcuts import get_object_or_404
from .forms import ActividadForm
from .forms import ServicioForm
from .forms import TipoActividadForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@login_required ( login_url = '/login/' )
def lista_actividades(request):

    a = Actividad.objects.all()
    return render(request, 'actividades/lista_actividades.html', {'a':a})

#metodo para detallar una actividad
@login_required ( login_url = '/login/' )
def detalle_actividad(request, id_actividad):

    b = get_object_or_404(Actividad, pk=id_actividad)

    return render(request, 'actividades/detalle_actividad.html', {'b':b})

#metodo para crear una nueva actividad
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def nueva_actividad(request):

    form_actividad = ActividadForm()

    if request.method == "POST":
        form_actividad = ActividadForm(request.POST)

        if form_actividad.is_valid():
            form_actividad.save()
            return render(request, "actividades/nueva_actividad_mesaje.html")

    return render(request,"actividades/nueva_actividad_form.html", {"form_actividad":form_actividad})

#metodo para editar una actividad
@login_required ( login_url = '/login/' )
def editar_actividad(request, id_actividad):
    instance = get_object_or_404(Actividad, pk=id_actividad)
    a = instance
    form = ActividadForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            a = Actividad.objects.all()
            mensaje= "Actividad Actualizada Correctamente"
            return render(request, 'actividades/lista_actividades.html', {'a': a,'mensaje':mensaje})
    return render(request, 'actividades/editar_actividad.html', {'form': form,'a':a})

#metodo para eliminar una actividad
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def eliminar_actividad(request, id_actividad):
     instance = get_object_or_404(Actividad, pk=id_actividad)
     a = instance
     if request.method == 'POST':
         instance.delete()
         a = Actividad.objects.all()
         b = "Actividad Eliminada Correctamente"
         return render(request, 'actividades/lista_actividades.html', {'a':a,'b':b})
     return render(request, 'actividades/eliminar_actividad.html', {'a':a})

@login_required ( login_url = '/login/' )
def lista_tipoActividades(request):

    a = TipoActividad.objects.all()

    return render(request, 'actividades/lista_tipoActividad.html', {'a':a})


#metodo para crear un nuevo Tipo De Actividad
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def nuevo_tipoActividad(request):

    form_tipoActividad = TipoActividadForm()

    if request.method == "POST":
        form_tipoActividad = TipoActividadForm(request.POST)

        if form_tipoActividad.is_valid():
            form_tipoActividad.save()
            a = TipoActividad.objects.all()
            b = "Se Agrego Correctamente El Tipo De Actividad"
            return render(request, "actividades/lista_tipoActividad.html",{"b":b,"a":a})

    return render(request,"actividades/nuevo_tipoActividad.html", {"form_tipoActividad":form_tipoActividad})

#metodo para detallar un Tipo de Actividad
@login_required ( login_url = '/login/' )
def detalle_tipoActividad(request, id_tipoactividad):

    b = get_object_or_404(TipoActividad, pk=id_tipoactividad)

    return render(request, 'actividades/detalle_tipoActividad.html', {'b':b})

#metodo para editar un Tipo de Actividad
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def editar_tipoActividad(request, id_tipoactividad):
    instance = get_object_or_404(TipoActividad, pk=id_tipoactividad)
    a = instance
    form = TipoActividadForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            a = TipoActividad.objects.all()
            b = "Tipo Actividad Actualizada Correctamente"
            return render(request, 'actividades/lista_tipoActividad.html', {'a': a,'b':b})
    return render(request, 'actividades/editar_tipoactividad.html', {'form': form,'a':a})

#metodo para eliminar un Tipo De Actividad
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def eliminar_tipoActividad(request, id_tipoactividad):
     instance = get_object_or_404(TipoActividad, pk=id_tipoactividad)
     a = instance
     if request.method == 'POST':
         instance.delete()
         a = TipoActividad.objects.all()
         b = "Tipo De Actividad Eliminada Correctamente"
         return render(request, 'actividades/lista_tipoActividad.html', {'a':a,'b':b})
     return render(request, 'actividades/eliminar_tipoActividad.html', {'a':a})

#metodo para crear un nuevo servicio
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def nuevo_servicio(request):

    form_servicio = ServicioForm()

    if request.method == "POST":
        form_servicio = ServicioForm(request.POST)

        if form_servicio.is_valid():
            form_servicio.save()
            return render(request, "actividades/nueva_actividad_mesaje.html")

    return render(request,"actividades/nuevo_servicio.html", {"form_servicio":form_servicio})

#metodo para listar los servicios
@login_required ( login_url = '/login/' )
def lista_servicios(request):

    a = Servicio.objects.all()

    return render(request, 'actividades/lista_servicios.html', {'a':a})

#metodo para editar servicio
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def editar_servicio(request, id_servicio):
    instance = get_object_or_404(Servicio, pk=id_servicio)
    a = instance
    form = ServicioForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            a = Servicio.objects.all()
            b = "Servicio Actualizado Correctamente"
            return render(request, 'actividades/lista_servicios.html', {'a': a,'b':b})
    return render(request, 'actividades/editar_servicio.html', {'form': form,'a':a})

#metodo para detallar un servicio
@login_required ( login_url = '/login/' )
def detalle_servicio(request, id_servicio):

    b = get_object_or_404(Servicio, pk=id_servicio)

    return render(request, 'actividades/detalle_servicio.html', {'b':b})

#metodo para eliminar un servicio
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def eliminar_servicio(request, id_servicio):
     instance = get_object_or_404(Servicio, pk=id_servicio)
     a = instance
     if request.method == 'POST':
         instance.delete()
         a = Servicio.objects.all()
         b = "Servicio Eliminado Correctamente"
         return render(request, 'actividades/lista_servicios.html', {'a':a,'b':b})
     return render(request, 'actividades/eliminar_servicio.html', {'a':a})
