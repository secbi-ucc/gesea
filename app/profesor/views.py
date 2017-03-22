from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Profesor
from .forms import ProfesorForm
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def agregar_profesor(request):
    user_form = UserForm()
    profile_form = ProfesorForm()
    mensaje = "Profesor"
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfesorForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            mensaje = "Profesor Agregado Correctamente"
            return render(request,'profesor/agregar_profesor.html',
            {'user_form': user_form, 'profile_form': profile_form,'mensaje':mensaje} )

    return render(request,'profesor/agregar_profesor.html',
    {'user_form': user_form, 'profile_form': profile_form,'mensaje':mensaje} )

#metodo para listar Usuarios Profesores
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def lista_profesores(request):
        profesores = Profesor.objects.all()
        paginator = Paginator(profesores, 25)
        page = request.GET.get('page')
        try:
            a = paginator.page(page)
        except PageNotAnInteger:
            a = paginator.page(1)
        except EmptyPage:
            a = paginator.page(paginator.num_pages)
        return render(request, 'Profesor/lista_profesores.html', {'a':a})

#metodo detallar un profesor
@user_passes_test(lambda u: u.is_superuser, login_url='/no-permitido/')
def detalle_profesor(request, id_ucc):

    b = get_object_or_404(Profesor, pk=id_ucc)

    return render(request, 'profesor/detalle_profesor.html', {'b':b})

def editar_profesor(request, id_ucc):
    instance = get_object_or_404(Profesor, pk=id_ucc)
    a = instance
    user_form = UserForm(request.POST or None, instance=instance.user)
    profile_form = ProfesorForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            a = Profesor.objects.all()
            mensaje = " Profesor Actualizado Correctamente!"
            return render(request, 'profesor/lista_profesores.html', {'a': a,'mensaje':mensaje})

    return render(request,'profesor/editar_profesor.html',
    {'user_form': user_form, 'profile_form': profile_form,'a':a})
