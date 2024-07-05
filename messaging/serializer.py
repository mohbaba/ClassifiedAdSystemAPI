from rest_framework import serializers

from messaging.models import Message
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'first_name', 'last_name']


class MessageSerializer(serializers.Serializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'content', 'time_sent']

    def create(self, validated_data):
        sender_data = validated_data.pop('sender')
        receiver_data = validated_data.pop('receiver')

        sender = User.objects.get(**sender_data)
        receiver = User.objects.get(**receiver_data)

        return Message(sender=sender, receiver=receiver, **validated_data)
