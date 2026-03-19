from multiprocessing import context
from django.contrib import messages  # type: ignore


from django.shortcuts import render,redirect, get_object_or_404 # type: ignore

import servicios
from servicios.forms import serviciosEditarForm, serviciosForm

def inicio(request):
    nombre = "Paula"
    context = {
        'nombre': nombre
    }
    return render(request, 'index.html', context)



# Create your views here.
