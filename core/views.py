from django.shortcuts import render

def inicio(request):
    nombre = "Paula"
    context = {
        'nombre': nombre
    }
    return render(request, 'index.html', context)



# Create your views here.
