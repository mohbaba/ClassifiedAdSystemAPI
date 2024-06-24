from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ads.models import Ad
from ads.serializer import AdSerializer, UserSerializer
from users.models import User


# Create your views here.

@api_view(['POST'])
def post_ad(request):
    print(request.data)
    serializer = AdSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

