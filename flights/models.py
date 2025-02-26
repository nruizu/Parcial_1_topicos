from django.db import models

# Create your models here.

class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64, choices=[('Domestic', 'Domestic'), ('International', 'International')])
    price = models.FloatField()