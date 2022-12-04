from django.http import Http404
from rest_framework import views, status
from rest_framework import authentication, permissions
from rest_framework.response import Response
from inventory.models import BakeryItem
from inventory.serializers import IngredientSerializers,BakeryItemsSerializers,BakeryItemsMiniSerializers


# Create your views here.

class BakeryProductManagement(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def get_object(self, pk):
        try:
            return BakeryItem.objects.get(pk=pk)
        except BakeryItem.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bakery_item = self.get_object(pk)
        serializer = BakeryItem(bakery_item)
        return Response(serializer.data)

    def put(self, request, pk):
        bakery_item = self.get_object(pk)
        serializer = IngredientSerializers(bakery_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        
        serializer = BakeryItemsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BakeryProductList(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self,request):
        bakery_items = BakeryItem.objects.all()
        serializer = BakeryItemsMiniSerializers(bakery_items, many=True)
        print(serializer.data)
        return Response(serializer.data)

