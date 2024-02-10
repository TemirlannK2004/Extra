from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50,null=True)

    def __str__(self) -> str:
        return f'Category: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(max_length=20,null=True)
    description = models.TextField(max_length = 2000)
    quantity = models.IntegerField(null=True)
    category_id = models.ForeignKey(Category,on_delete = models.CASCADE,null=True)
    is_active = models.BooleanField(default = True)

    def __str__(self) -> str:
        return f'Product:{self.name} ({self.category_id})'
    
    
class Order(models.Model):
    product_id = models.ForeignKey(Product,on_delete = models.CASCADE)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f'{self.user_id.id}: {self.product_id.name} - {self.created_at}'