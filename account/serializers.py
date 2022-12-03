from account.models import BillingAddress
from django.contrib.auth.models import User
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'password', 'email','address']

    def create(self, validated_data):
        address = validated_data.pop('address')
        instance = User.objects.create(**validated_data)
        ba = BillingAddress.objects.create(customer = instance,**address)
        ba.first_name = instance.first_name
        ba.last_name = instance.last_name
        ba.save()
        return instance
    
    