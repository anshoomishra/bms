from django.urls import path

from .views import BakeryProductManagement,BakeryProductList

urlpatterns = [
    path('manage-bakery/', BakeryProductManagement.as_view()),
    path('available-products/', BakeryProductList.as_view()),
]