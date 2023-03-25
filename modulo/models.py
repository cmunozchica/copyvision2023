from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
TIPO_CHOICES = (
    ('COTIZACION', 'COTIZACION'),
    ('ORDEN DE TRABAJO', 'ORDEN DE TRABAJO'),
)
TRABAJO_CHOICES = (
    ('GRAN-FORMATO', 'GRAN-FORMATO'),
    ('CORTE-LASER Y GRABADO', 'CORTE-LASER Y GRABADO'),
    ('IMPRESIONES', 'IMPRESIONES'),
    ('PUBLICIDAD', 'PUBLICIDAD'),
)

ESTADO_CHOICES = (
    ('COTIZAR', 'COTIZAR'),
    ('COTIZADO', 'COTIZADO'),
    ('EN PROCESO', 'EN PROCESO'),
    ('LISTO', 'LISTO'),
    ('ENTREGADO', 'ENTREGADO'),
)


class Trabajo(models.Model):
    nit = models.CharField(max_length=15, null=True)
    cliente = models.CharField(max_length=30, )
    direccion = models.CharField(max_length=30, null=True)
    telefono = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add=True)
    fechaEntrega = models.DateTimeField(verbose_name='Fecha Entrega')
    descripcion = models.TextField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    tipoTrabajo = models.CharField(max_length=30, choices=TRABAJO_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    class Meta:
        verbose_name = 'trabajo'
        verbose_name_plural = 'trabajos'

    def __str__(self):
        return self.nit
    
CATEGORIA_CHOICES = (
    ('PAPELERIA', 'PAPELERIA'),
    ('PAPEL', 'PAPEL'),
    ('PLOTTER', 'PLOTTER'),
    ('PUBLICIDAD', 'PUBLICIDAD'),
    ('VARIOS', 'VARIOS'),
)
    

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)    
    precio = models.FloatField()
    cantidad = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return '{} - {} - {} - {} '.format(
            self.id,
            self.nombre,            
            self.precio,
            self.cantidad

            
        )