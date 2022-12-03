from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from account.serializers import RegistrationSerializer


@api_view(['GET', 'POST'])
@permission_classes([])
def registration_view(request):
    """
    this function is used for registering a user into the system.
    :param request:
    :return:
    """
    
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.get(user=user).key
        response = dict(message='successfully registered.', token=token)
        return Response(response, status=status.HTTP_200_OK)
    else:
        
        response = serializer.errors
        print("Res",response)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)