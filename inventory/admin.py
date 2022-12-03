from django.contrib import admin
from .models import BakeryItem,Ingredients
# Register your models here.

admin.site.register(Ingredients)
admin.site.register(BakeryItem)
