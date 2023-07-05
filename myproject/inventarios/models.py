from django.db import models

# Create your models here.

class Productos(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField()
  existence = models.IntegerField()

