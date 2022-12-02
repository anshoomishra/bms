from django.db import models

# Create your models here.
from inventory.models import BakeryItem
from django.conf import settings




class Order(models.Model):
    bakery_item = models.ForeignKey(BakeryItem,on_delete=models.PROTECT)
    ordered_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    
    class Meta:
        ordering = ["-created_at"]

class Bill(models.Model):
    title = models.CharField(max_length=100)
    order = models.OneToOneField(Order,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
    
    