from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.views import login



def inicio(request):


    return render(request, 'core/inicio.html', {})

def no_permitido(request):


    return render(request, 'core/no_permitido.html', {})
