from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True) 
    
    def __str__(self):
        return self.name