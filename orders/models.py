import math

from django.db import models

# Create your models here.
from django.db.models.signals import post_save, pre_save

from inventory.models import BakeryItem

from account.models import User, BillingAddress
from orders.utils import unique_order_id_generator

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


class OrderQuerySet(models.QuerySet):
    """
    User For Filtering Some Data
    """
    def recent(self):
        return self.order_by("-updated", "-timestamp")
    
    def cancelled_orders(self, user):
        return self.filter(ordered_by=user).filter(is_cancelled=True)


class OrderManager(models.Model):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)
    
    def get_cancelled_orders(self, user):
        return self.get_queryset().cancelled_orders(user)


class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True)
    bakery_item = models.ManyToManyField(BakeryItem, related_name="items")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    is_cancelled = models.BooleanField(default=False)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES, null=False)
    transaction_id = models.CharField(max_length=256, unique=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='IP')
    shipping_address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE,related_name="shipping_address", null=True, blank=True)
    billing_address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE,related_name="billing_address", null=True, blank=True)
    total_amount = models.IntegerField(null=False)
    
    class Meta:
        ordering = ["-created_at"]
    
    def update_total(self):
        item_total = 0
        items = self.bakery_item.all()
        print(items)
        for item in items:
            print(item.selling_price)
            item_total += item.selling_price
        
        self.total_amount = item_total
        
        self.save()
        return self.total_amount


def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        print("Updating... first")
        print(instance)
        instance.update_total()


# post_save.connect(post_save_order, sender=Order)


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=Order)
