from django import forms
from django.contrib.auth.models import User
from .models import Instructor


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username', 'password')

class ProfesorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = ['id_ucc','Identificacion','estado']
