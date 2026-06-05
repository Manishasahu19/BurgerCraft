from django.db import models

# Create your models here.
from django.db import models

class Burger(models.Model):
   
    name = models.CharField(max_length=200)
    
   
    category = models.CharField(max_length=100, default='Snacks')
    
    
    price = models.DecimalField(max_digits=6, decimal_places=2)
   
    description = models.TextField()
    
   
    image_url = models.URLField(max_length=500)
    
    
    def __str__(self):
        return self.name