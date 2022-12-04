from django.urls import path

from .views import create_order, OrderHistoryView, OrderHistoryFilterView

urlpatterns = [
    path('submit-order/', create_order),
    path('my-orders/', OrderHistoryView.as_view()),
    path('my-orders/filter/', OrderHistoryFilterView.as_view()),
]