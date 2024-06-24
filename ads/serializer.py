from rest_framework import serializers

from ads.models import Ad
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number']


class AdSerializer(serializers.ModelSerializer):
    uploader = UserSerializer()

    class Meta:
        model = Ad
        fields = ['title', 'description', 'category', 'image', 'price', 'uploader']

    def create(self, validated_data):
        uploader_data = validated_data.pop('uploader')
        uploader = User.objects.get(phone_number=uploader_data['phone_number'])
        ad = Ad.objects.create(uploader=uploader, **validated_data)
        return ad





#
# from rest_framework import serializers
# from ads.models import Ad
# from users.models import User
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['phone_number']
#
#
# class AdSerializer(serializers.ModelSerializer):
#     uploader = UserSerializer()
#
#     class Meta:
#         model = Ad
#         fields = ['title', 'description', 'category', 'image', 'price']
#
#     def create(self, validated_data):
#         uploader_data = validated_data.pop('uploader')
#
#         try:
#             uploader = User.objects.get(phone_number=validated_data['phone_number'])
#             ad = Ad.objects.create(uploader=uploader, **validated_data)
#         except User.DoesNotExist:
#             raise serializers.ValidationError("Uploader with this phone number does not exist")
#
#         return ad
