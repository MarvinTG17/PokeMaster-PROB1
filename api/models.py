from django.db import models
from django.db.models.fields import CharField, URLField,IntegerField

class Pokemon(models.Model): 
    identifier      = CharField(max_length=100)
    species_id      = IntegerField() 
    height          = IntegerField() 
    weight          = IntegerField() 
    base_experience = IntegerField() 
    order           = IntegerField()
    is_default      = IntegerField()  

class Pokedex(models.Model): 
    region_id       = IntegerField() 
    identifier      = CharField(max_length=100)
    is_main_series  = IntegerField() 
