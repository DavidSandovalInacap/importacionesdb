# aqui se define el modelo de datos utilizando Django's ORM
from django.db import models

# Create your models here.
class Importacion(models.Model):
    # Definiendo los campos del modelo Importacion
    id = models.AutoField(primary_key=True)
    nombre_articulo = models.CharField(max_length=20, verbose_name="Nombre articulo")
    nombre_proveedor = models.CharField(max_length=20)
    unidades = models.PositiveIntegerField()
    costo_unitario = models.PositiveIntegerField()
    costo_envio = models.PositiveIntegerField()
    codigo_articulo = models.CharField(max_length=20, verbose_name="Codigo")
    imagen_producto = models.ImageField(upload_to='iamgenes/',verbose_name="Imagen del producto", null=True)
    
    def __str__(self):
        fila = "Nombre articulo: " + self.nombre_articulo + " - " + "Codigo: " + self.codigo_articulo
        return fila
    
    
class Boleta(models.Model):
    # Definiendo los campos del modelo Boleta
    id_importacion = models.ForeignKey(Importacion, on_delete=models.CASCADE)
    total_importacion = models.PositiveIntegerField()
    costo_envio = models.PositiveIntegerField()
    cif = models.PositiveIntegerField()
    tasa_aduana = models.PositiveIntegerField()
    iva = models.PositiveIntegerField()
    impuestos = models.PositiveIntegerField()
    total_compra = models.PositiveIntegerField()
    valor_dolares = models.PositiveIntegerField()

    def __str__(self):
        return f"Boleta {self.id_importacion.id}"