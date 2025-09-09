from rest_framework import serializers

from .models import JWTUsers

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