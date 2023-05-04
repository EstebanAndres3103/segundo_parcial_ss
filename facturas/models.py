from django.db import models

# Create your models here.

class Cliente(models.Model):
    nit = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

class Helado(models.Model):
    id_helado = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    sabor = models.CharField(max_length=50)
    tam=models.CharField(max_length=20)
    precio = models.CharField(max_length=5)

class Topping(models.Model):
    id_topping = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class DetalleFactura(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    helado = models.ForeignKey(Helado, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
