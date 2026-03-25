from django import forms
from .models import Producto, Stock, Compra, DetalleCompra


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['nombre', 'descripcion']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio_venta', 'precio_compra', 'stock']


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['nombre_cliente', 'correo', 'telefono', 'direccion', 'metodo_pago', 'total']


class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'compra', 'cantidad', 'subtotal']


# 🔥 FORMULARIO DE PAGO
class PagoForm(forms.Form):
    nombre = forms.CharField()
    correo = forms.EmailField()
    telefono = forms.CharField()
    direccion = forms.CharField()

    metodo_pago = forms.ChoiceField(
        choices=[
            ('persona', 'Pago en persona'),
            ('contraentrega', 'Pago contraentrega')
        ]
    )