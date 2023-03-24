from django.db import models
from . import views 

# Create your models here
class Item(models.Model):
    description = models.CharField(max_length=50)