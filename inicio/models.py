from django.db import models



class Auto(models.Model):

    modelo = models.CharField(max_length=30)

    marca = models.CharField(max_length=30)  

    imagen = models.ImageField(upload_to='imagenes_autos', null=True) 

    year = models.IntegerField(null=True, blank=True)

    kilometros = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Auto({self.id}): {self.marca} - {self.modelo} ({self.year})'

