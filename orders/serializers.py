from rest_framework import serializers

from account.models import BillingAddress
from .models import Order
from inventory.serializers import BakeryItemsSerializers
from inventory.models import BakeryItem


class OrderSerializers(serializers.ModelSerializer):
    bakery_item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'
    

    
    
