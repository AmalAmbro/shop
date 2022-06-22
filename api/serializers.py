from django.http import HttpRequest
from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Shop


class ShopSerializer( serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = '__all__'


    def get_image_url(self, instance):
        if self.context:
            request = self.context['request']
            return request.build_absolute_uri(instance.image)
        else:
            return None

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
