from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    nombre_completo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Juan Pérez'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control custom-input', 'placeholder': 'correo@email.com'})
    )
    telefono = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': '3001234567'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control custom-input', 'placeholder': '••••••••'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control custom-input', 'placeholder': '••••••••'})
    )

    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Ej: juan_barber'}),
        }