from django import forms
from django.contrib.auth.models import User
from .models import Profesor


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username', 'password')

class ProfesorForm(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = ['id_ucc','Identificacion','estado']
