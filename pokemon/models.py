from django.db import models

class Pokemon(models.Model):
    id_table = models.AutoField(primary_key=True)
    id_pokemon = models.CharField(max_length=100)
    name = models.CharField(max_length=100,blank=True, null=True)
    height = models.CharField(max_length=100,blank=True, null=True)
    weight = models.CharField(max_length=100,blank=True, null=True)
    evolutions = models.CharField(max_length=150,blank=True, null=True)
    stat = models.CharField(max_length=200,blank=True, null=True)
    
