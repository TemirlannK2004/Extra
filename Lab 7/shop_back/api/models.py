from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,null=True)

    def __str__(self) -> str:
        return f'Category: {self.name}'

class Product(models.Model):
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(max_length=20,null=True)
    description = models.TextField(max_length = 2000)
    quantity = models.IntegerField(null=True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE,null=True)
    is_active = models.BooleanField(default = True)

    def __str__(self) -> str:
        return f'Product:{self.name} ({self.category})'