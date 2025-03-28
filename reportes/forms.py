from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Equipo, ReporteDanio

# Formulario para registrar equipos (ya lo tenemos)
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'tipo', 'descripcion', 'ubicacion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

# Formulario para reportar daños (ya lo tenemos)
class ReporteDanioForm(forms.ModelForm):
    class Meta:
        model = ReporteDanio
        fields = ['equipo', 'descripcion_danio', 'estado']
        widgets = {
            'descripcion_danio': forms.Textarea(attrs={'rows': 3}),
        }

# Nuevo formulario para registro de usuarios
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']