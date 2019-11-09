from rest_framework import generics
from .models import Demands, UserDetails
from .ModelSerializer import DemandsSerializer, UserSerializer, UserDetailSerializer
from django.contrib.auth.models import User


class DemandsListAPI(generics.ListCreateAPIView):
    queryset = Demands.objects.all()
    serializer_class = DemandsSerializer


class UserDetailsList(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
