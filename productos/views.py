from django.shortcuts import render

def productos(request):
    return render(request, 'Productos.html')

def carrito(request):
    return render(request, 'Carrito.html')

def carrito(request):
    return render(request, 'pago.html')