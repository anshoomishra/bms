import uuid
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import views, generics, status, authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.serializers import AddressSerializer
from .models import Order
from .serializers import OrderSerializers
from inventory.models import BakeryItem
from account.models import User, BillingAddress
import json

# Create your views here.

class OrderHistoryView(generics.ListAPIView):
    
    """
    Added Few QuerySet Methods in Model to apply few searching
    
    """
    authentication_classes = [TokenAuthentication]
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset().filter(buyer=request.user)
        serializer = OrderSerializers(queryset, many=True)
        return Response(serializer.data)

class OrderHistoryFilterView(generics.ListAPIView):
    
    """
    To Use Basic Filtering On Order
    """
    
    authentication_classes = [TokenAuthentication]
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order_id', 'is_cancelled','payment_type']
    
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def create_order(request):
    
    error = False
    
    try:
        item_ids = request.data.get('bakery_item', None)
        if not item_ids:
            error = True
            message = "Please attach an item_id with the request."
            return
        all_bakery_items = []
        total = 0
        for item in item_ids:
            item = BakeryItem.objects.get(id=item)
            total += item.selling_price
            all_bakery_items.append(item)
        address = BillingAddress.objects.filter(customer=request.user).first()
       
        order = Order.objects.create(
                buyer=request.user,
                created_at=datetime.now(),
                payment_type=request.data.get('payment_type', 'COD'),
                shipping_address=address,
                transaction_id=uuid.uuid4().hex,
                total_amount=0.0
            )
        
        order.bakery_item.set(all_bakery_items)
        order.total_amount = total
        order.save()
        
        message = "Thank you for placing your order with us.\nHere's your invoice."
        customer = User.objects.get(username=request.user.username)
        invoice = {
                'transaction_id': order.transaction_id,
                'buyer': order.buyer.username,
                'item': order.bakery_item.name,
                'order_date': order.created_at,
                'total_amount': order.total_amount,
                'payment_type': order.payment_type,
                'shipping_address':AddressSerializer(address).data
        
            }
            
    except ObjectDoesNotExist:

        error = True
        message = "Sorry, you seem to have an id of an item which isn't available with us."

    except Exception as e:
        error = True
        
        message = "Sorry, some error occurred at our end, please try again later."
        raise e
    finally:
        if not error:
            return Response({
                'message': message,
                'invoice': invoice
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': message
            }, status=status.HTTP_400_BAD_REQUEST)

