from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required


def inicio(request):


    return render(request, 'core/inicio.html', {})

@login_required ()
def no_permitido(request):


    return render(request, 'core/no_permitido.html', {})



