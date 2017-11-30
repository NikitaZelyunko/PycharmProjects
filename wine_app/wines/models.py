from django.db import models


# Create your models here.

class WineItem(models.Model):
    id = models.PositiveIntegerField(default=0, primary_key=True)
    inStock = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    picture = models.URLField(default="")
    year = models.IntegerField(default=0)
    color = models.CharField(max_length=10, default="")
    type_wine = models.CharField(max_length=40, default="")
    city = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    company = models.CharField(max_length=50, default="")
    about = models.TextField(default="")
    tags = models.TextField(default="")




