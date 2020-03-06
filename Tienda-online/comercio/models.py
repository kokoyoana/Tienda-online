from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length = 20, null = False)
    descripcion = models.TextField(blank = False,null = False)
    precio = models.FloatField(default = 10, null= True)
    stock = models.IntegerField(default = 10, null= True)
    tipo = models.CharField(max_length=1,null=True)
    imagen = models.ImageField(upload_to='static/imgPro')

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    subTotal = models.FloatField(blank = False,null = False)
    cantidad = models.IntegerField(default = 1, null= True)
    idPro = models.ForeignKey(Producto, on_delete=models.CASCADE, null= True)
    idUser = models.IntegerField(default = 1, null= True)
    
    def __str__(self):
        return self.idPro

