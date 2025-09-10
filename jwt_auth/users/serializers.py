from rest_framework import serializers

from .models import JWTUsers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = JWTUsers
        fields = ['password', 'email', 'username']
    
    def create(self, validated_data):
        return JWTUsers.objects.create_user(**validated_data)
        

class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = JWTUsers
        fields = '__all__'
        
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        
        return token