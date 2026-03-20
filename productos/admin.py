from django.contrib import admin
from .models import Producto, Stock, Compra, DetalleCompra

admin.site.register(Producto)
admin.site.register(Stock)
admin.site.register(Compra)
admin.site.register(DetalleCompra)
# Register your models here.
