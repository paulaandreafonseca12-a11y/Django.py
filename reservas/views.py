from django.shortcuts import render

# Create your views here.

def reservas_view(request):
    context = {
    'titulo' : 'Reserva el corte que desees'
    }
    return render(request, 'reservas.html', context)

def calificacion_view(request):
    context = {
    'titulo' : 'Califica tu experiencia'
    }
    return render(request, 'calificacion.html', context)