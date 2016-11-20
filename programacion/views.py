from django.shortcuts import render
from .models import Programacion,Lugar,Horario, DiaActividad
from django.shortcuts import get_object_or_404
from .forms import ProgramacionForm
from .forms import LugarForm
from .forms import DiaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#metodo para listar horarios
@login_required ( login_url = '/login/' )
def horario_lista(request):
    horarios = Horario.objects.all()
    paginator = Paginator(horarios, 25)
    page = request.GET.get('page')
    try:
        a = paginator.page(page)
    except PageNotAnInteger:
        a = paginator.page(1)
    except EmptyPage:
        a = paginator.page(paginator.num_pages)

    return render(request, 'programacion/lista_horarios.html', {'a':a})

#metodo para eliminar un horario
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def horario_eliminar(request, id_horario):
     instance = get_object_or_404(Horario, pk=id_horario)
     a = instance
     if request.method == 'POST':
         instance.delete()
         a = Horario.objects.all()
         b = "Horario Eliminado Correctamente"
         return render(request, 'programacion/lista_horarios.html', {'a':a,'b':b})
     return render(request, 'programacion/eliminar_horario.html', {'a':a})


#metodo para detallar horario
@login_required ( login_url = '/login/' )
def horario_detalle(request, id_horario):

    b = get_object_or_404(Horario, pk=id_horario)

    return render(request, 'programacion/detalle_horario.html', {'b':b})


#metodo para listar dias y su horario
@login_required ( login_url = '/login/' )
def dias_lista(request):
    dias = DiaActividad.objects.all()
    paginator = Paginator(dias, 25)
    page = request.GET.get('page')
    try:
        a = paginator.page(page)
    except PageNotAnInteger:
        a = paginator.page(1)
    except EmptyPage:
        a = paginator.page(paginator.num_pages)

    return render(request, 'programacion/lista_dias.html', {'a':a})

#metodo para agregar un nuevo dia y su horario
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def dia_nuevo(request):

    form_dia = DiaForm()

    if request.method == "POST":
        form_dia = DiaForm(request.POST)
        if form_dia.is_valid():
            form_dia.save()
            a = DiaActividad.objects.all()
            return render(request, "programacion/lista_dias.html", {"a":a})

    return render(request,"programacion/nuevo_dia.html", {"form_dia":form_dia})

#metodo para detalllar un dia y su horario
login_required ( login_url = '/login/' )
def dia_detalle(request, id_dia):

    b = get_object_or_404(DiaActividad, pk=id_dia)

    return render(request, 'programacion/detalle_dia.html', {'b':b})

#metodo para editar un dia y su horario
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def dia_editar(request, id_dia):
    instance = get_object_or_404(DiaActividad, pk=id_dia)
    a = instance
    form = DiaForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            a = DiaActividad.objects.all()
            mensaje= "Dia Actualizado Correctamente"
            return render(request, 'programacion/lista_dias.html', {'a': a,'mensaje':mensaje})
    return render(request, 'programacion/editar_dia.html', {'form': form,'a':a})

#metodo para eliminar un dia y su horario
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def dia_eliminar(request, id_dia):
     instance = get_object_or_404(DiaActividad, pk=id_dia)
     a = instance
     if request.method == 'POST':
         instance.delete()
         a = DiaActividad.objects.all()
         b = "Dia Eliminado Correctamente"
         return render(request, 'programacion/lista_dias.html', {'a':a,'b':b})
     return render(request, 'programacion/eliminar_dia.html', {'a':a})

#metodo para listar lugares
@login_required ( login_url = '/login/' )
def lugares_lista(request):
    lugares = Lugar.objects.all()
    paginator = Paginator(lugares, 25)
    page = request.GET.get('page')
    try:
        a = paginator.page(page)
    except PageNotAnInteger:
        a = paginator.page(1)
    except EmptyPage:
        a = paginator.page(paginator.num_pages)

    return render(request, 'programacion/lista_lugar.html', {'a':a})

#metodo para agregar un nuevo lugar
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def lugar_nuevo(request):

    form_lugar = LugarForm()

    if request.method == "POST":
        form_lugar = LugarForm(request.POST)
        if form_lugar.is_valid():
            form_lugar.save()
            a = Lugar.objects.all()
            return render(request, "programacion/lista_lugar.html", {"a":a})

    return render(request,"programacion/nuevo_lugar.html", {"form_lugar":form_lugar})

#metooddo para detallar un lugar
@login_required ( login_url = '/login/' )
def lugar_detalle(request, id_lugar):

    b = get_object_or_404(Lugar, pk=id_lugar)

    return render(request, 'programacion/detalle_lugar.html', {'b':b})

#metodo para editar lugar
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def lugar_editar(request, id_lugar):
    instance = get_object_or_404(Lugar, pk=id_lugar)
    a = instance
    form = LugarForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            a = Lugar.objects.all()
            mensaje= "Lugar Actualizado Correctamente"
            return render(request, 'programacion/lista_lugar.html', {'a': a,'mensaje':mensaje})
    return render(request, 'programacion/editar_lugar.html', {'form': form,'a':a})

#meetdo para eliminar un lugar
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def lugar_eliminar(request, id_lugar):
     instance = get_object_or_404(Lugar, pk=id_lugar)
     a = instance
     if request.method == 'POST':
         instance.delete()
         a = Lugar.objects.all()
         b = "Lugar Eliminado Correctamente"
         return render(request, 'programacion/lista_lugar.html', {'a':a,'b':b})
     return render(request, 'programacion/eliminar_lugar.html', {'a':a})


#metodo para listar todas las programaciones
@login_required ( login_url = '/login/' )
def programacion_lista(request):

    a = Programacion.objects.all()

    return render(request, 'programacion/lista_programacion.html', {'a':a})

#metodo para agregar una nueva programacion
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def programacion_nueva(request):
    form_programacion = ProgramacionForm()

    if request.method == "POST":
        form_programacion = ProgramacionForm(request.POST)
        if form_programacion.is_valid():
            form_programacion.save()
            a = Programacion.objects.all()
            return render(request, 'programacion/lista_programacion.html', {'a':a})

    return render(request, 'programacion/nueva_programacion.html', {'form_programacion':form_programacion})

@login_required ( login_url = '/login/' )
def programacion_detalle(request, id_programacion):

    b = get_object_or_404(Programacion, pk=id_programacion)

    return render(request, 'programacion/detalle_programacion.html', {'b':b})

#metodo para eliminar una programacion
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def programacion_eliminar(request, id_programacion):
     instance = get_object_or_404(Programacion, pk=id_programacion)
     a = instance
     if request.method == 'POST':
         instance.delete()
         a = Programacion.objects.all()
         b = "Programacion Eliminada Correctamente"
         return render(request, 'programacion/lista_programacion.html', {'a':a,'b':b})
     return render(request, 'programacion/eliminar_programacion.html', {'a':a})
