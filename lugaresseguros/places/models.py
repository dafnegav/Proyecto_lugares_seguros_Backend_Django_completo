from django.db import models
from django.forms import CharField

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=56)
    description = models.CharField(max_length=256)
    address_state = models.CharField(max_length=32)
    address_city = models.CharField(max_length=32)
    address_colonia = models.CharField(max_length=32)
    address_street = models.CharField(max_length=32)
    address_zipcode = models.CharField(max_length=32)
    
    class Meta: #declaro una clase Meta con el nombre de la tabla
        db_table = 'places'

    def __str__(self): #retorno un string representativo quesea 
        #leible por nosotros al momento de ejecutar una sentencia
        return self.name

