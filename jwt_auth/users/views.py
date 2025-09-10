from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegisterSerializer, AllUserSerializer, MyTokenObtainPairSerializer
from .models import JWTUsers
# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    queryset = JWTUsers.objects.all()
    serializer_class = UserRegisterSerializer
    
class AllUserView(generics.ListAPIView):
    queryset = JWTUsers.objects.all()
    serializer_class = AllUserSerializer
    permission_classes = [IsAuthenticated]
    
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer