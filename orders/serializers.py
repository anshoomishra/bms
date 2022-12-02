from rest_framework.serializers import ModelSerializer
from .models import Order


class OrderSerializers(ModelSerializer):
    class Meta:
        models = Order
        fields = '__all__'