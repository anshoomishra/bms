from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL


class Ingredients(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()  # Considering units here
    cost_price = models.FloatField()
    
    
class BakeryItem(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ForeignKey(Ingredients,on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    expiry_date = models.DateTimeField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    selling_price = models.FloatField()
    is_available = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name
    

class Inventory(models.Model):
    bakery_item = models.ManyToManyField(BakeryItem)
    sku = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    quantity = models.IntegerField() # number of Bakery Items Available
    
    class Meta:
        permissions = [("can_manage_inventory", "Can Manage Inventory")]
