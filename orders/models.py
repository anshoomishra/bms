from django.db import models

# Create your models here.
from inventory.models import BakeryItem
from django.conf import settings
from account.models import User
PAYMENT_CHOICES = (
    ('COD', 'COD'),
    ('Card', 'Card'),
    ('UPI', 'UPI'),
    ('Wallet', 'Wallet'),
)

ORDER_STATUS = (
    ('IP', 'In Processing'),
    ('OH', 'On Hold'),
    ('C', 'Cancelled'),
    ('OFD', 'Out For Delivery'),
    ('R', 'Returned'),
    ('D', 'Delivered'),
)


class Order(models.Model):
    bakery_item = models.ForeignKey(BakeryItem,on_delete=models.PROTECT)
    ordered_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    is_cancelled = models.BooleanField(default=False)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES, null=False)
    shipping_address = models.CharField(max_length=100, blank=True, null=False)
    transaction_id = models.CharField(max_length=256, unique=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='IP')
    quantity = models.IntegerField(null=False, default=1)
    total_amount = models.IntegerField(null=False)
    class Meta:
        ordering = ["-created_at"]

class Bill(models.Model):
    title = models.CharField(max_length=100)
    order = models.OneToOneField(Order,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    
    
    