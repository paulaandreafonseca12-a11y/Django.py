from django.shortcuts import render, redirect
from .models import Compra, Producto
from django.contrib import messages
def productos(request):
    return render(request, 'Productos.html')

def carrito(request):
    return render(request, 'Carrito.html')

def pago(request):
    return render(request, 'pago.html')


def procesar_compra(request):
    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        metodo_pago = request.POST.get('metodo_pago')
        total = request.POST.get('total')

        Compra.objects.create(
            nombre_cliente=nombre,
            correo=correo,
            telefono=telefono,
            direccion=direccion,
            metodo_pago=metodo_pago,
            total=total
        )

        # 🔥 MENSAJE
        messages.success(request, "✅ Compra realizada con éxito")

        return redirect('Productos.html')

    return redirect('Productos.html')

def Producto(request):
    if request.method == 'POST':
        form = Producto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crear_producto')
    else:
        form = Producto()

    return render(request, 'crear_producto.html', {'form': form})