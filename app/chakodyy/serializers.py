from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from accounts.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UpdateUserInfo(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'address', 'city', 'country', 'phone']
        extra_kwargs = {'email': {'required': True}}

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user.username = attrs.get("username")
            user.email = attrs.get("email")
            user.last_name = attrs.get("last_name")
            user.first_name = attrs.get("first_name")
            user.last_name = attrs.get("last_name")
            user.address = attrs.get("address")
            user.city = attrs.get("city")
            user.country = attrs.get("country")
            user.phone = attrs.get("phone")
            user.save()
        return attrs


class TokenObtainSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['username']

    def validate(self, data):
        if not ('@' in data.get('email')):
            try:
                user = User.objects.get(username=data.get('email'))
                email = user.email
            except User.DoesNotExist:
                raise serializers.ValidationError("No such user exists")
        else:
            email = data.get('email')

        credentials = {
            "email": email,
            "password": data.get("password")
        }
        data = super().validate(credentials)

        return data


class UpdatePasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'email': {'required': True}}

    def validate(self, data):

        if not ('@' in data.get('email')):
            try:
                user = User.objects.get(username=data.get('email'))
            except User.DoesNotExist:
                raise serializers.ValidationError("No such user exists")
        else:
            try:
                user = User.objects.get(email=data.get('email'))
            except User.DoesNotExist:
                raise serializers.ValidationError("No such user exists")

        user.set_password(data.get('password'))
        user.save()
        return data


# class SocialSerializer(serializers.Serializer):
#     """
#     Serializer which accepts an OAuth2 access token and provider.
#     """
#     provider = serializers.CharField(max_length=255, required=True)
#     access_token = serializers.CharField(max_length=4096, required=True, trim_whitespace=True)
