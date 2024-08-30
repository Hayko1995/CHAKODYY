from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers

class CustomUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone',
            'role'
            )