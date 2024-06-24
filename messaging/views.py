from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK

from messaging.models import Message
from messaging.serializer import MessageSerializer
from users.models import User


# Create your views here.

@api_view(['POST'])
def send_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_messages(request, sender_phone, receiver_phone):
    sender = User.objects.get(phone_number=sender_phone)
    receiver = User.objects.get(phone_number=receiver_phone)
    messages = Message.objects.all().filter(sender=sender, receiver=receiver)
    serializer = MessageSerializer(messages, many=True)

    return Response(serializer.data, status=HTTP_200_OK)


def test_view(request, sender_phone, receiver_phone):
    return HttpResponse(f"sender:{sender_phone} receiver:{receiver_phone}")
