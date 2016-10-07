from django import forms
from .models import Actividad

class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ['servicio', 'tipo_actividad', 'Estado_actividad', 'Cupo_Actividad','Estado_actividad']
