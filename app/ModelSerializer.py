from rest_framework import serializers

from app.models import Demands, UserDetails
from django.contrib.auth.models import User


class DemandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demands
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
