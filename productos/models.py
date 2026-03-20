from django.db import models


class Stock(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    codigo_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name="productos"
    )

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    codigo_compra = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.nombre_cliente} - Compra {self.codigo_compra}"


class DetalleCompra(models.Model):
    codigo_detalle = models.AutoField(primary_key=True)

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )

    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name="detalles"
    )

    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.codigo_detalle}"


class Pago(models.Model):
    compra = models.ForeignKey('Compra', on_delete=models.CASCADE)

    METODOS_PAGO = [
        ('persona', 'Pago en persona'),
        ('contraentrega', 'Pago contraentrega'),
    ]

    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.nombre}"