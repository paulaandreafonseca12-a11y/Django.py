from django.shortcuts import render

# Create your views here.

def servicios_view(request):
    context = {
    'titulo' : 'Nuestros Servicios'
    }
    return render(request, 'servicios.html', context)
