from django.shortcuts import render

from rest_framework import generics

from .serializers import UserRegisterSerializer, AllUserSerializer
from .models import JWTUsers
# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    queryset = JWTUsers.objects.all()
    serializer_class = UserRegisterSerializer
    
class AllUserView(generics.ListAPIView):
    queryset = JWTUsers.objects.all()
    serializer_class = AllUserSerializer