from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.conf import settings
from datetime import timedelta

# Create your models here.

User = settings.AUTH_USER_MODEL


def expiration_date():
    now = timezone.now() + timedelta(days=365)
    return now


class Ingredients(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()  # Considering units here
    cost_price = models.FloatField()
    
    def __str__(self):
        return self.name


class BakeryItem(models.Model):
    name = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(default=expiration_date, verbose_name='Expirate in')
    selling_price = models.FloatField(default=10)
    is_available = models.BooleanField(default=True)
    discount = models.FloatField(default=0.0)
    cost_price = models.FloatField(default=0.0)
    profit = models.FloatField(default=0.0)
    ingredients = models.ManyToManyField(Ingredients)
    
    def __str__(self):
        return self.name
    
    
class Inventory(models.Model):
    bakery_item = models.ManyToManyField(BakeryItem)
    sku = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    quantity = models.IntegerField()  # number of Bakery Items Available
    
    class Meta:
        permissions = [("can_manage_inventory", "Can Manage Inventory")]
