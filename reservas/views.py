from django.shortcuts import render

# Create your views here.

def reservas_view(request):
    context = {
    'titulo' : 'Reserva el corte que desees'
    }
    return render(request, 'reservas.html', context)