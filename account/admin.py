from django.contrib import admin
from .models import BillingAddress
from rest_framework.authtoken.models import Token
# Register your models here.


admin.site.register(BillingAddress)
