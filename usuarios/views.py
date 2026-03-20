from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Ciframos la contraseña para que Django pueda validarla después
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login') # Nombre de la ruta en tu urls.py
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})