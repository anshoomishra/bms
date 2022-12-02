from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User
from django_countries.fields import CountryField
from phonenumber_field import PossiblePhoneNumberField
# Create your models here.

class BillingAddress(models.Model):

    '''
    Taking BillingAddress to get help in generating Bill after
    Putting Orders

    '''
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    company_name = models.CharField(max_length=256, blank=True)
    street_address_1 = models.CharField(max_length=256, blank=True)
    street_address_2 = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    city_area = models.CharField(max_length=128, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = CountryField()
    country_area = models.CharField(max_length=128, blank=True)
    phone = PossiblePhoneNumberField(blank=True, default="")

    def __str__(self) -> str:
        return self.street_address_1 + self.street_address_2

class User(AbstractBaseUser):
    '''
    Custom User class For extra attributes

    '''
    first_name = models.CharField(max_length=256,blank=True)
    last_name = models.CharField(max_length=256,blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    address  = models.ManyToManyField(BillingAddress,blank=True, related_name="user_addresses")
    def __str__(self) -> str:
        return self.first_name
    


