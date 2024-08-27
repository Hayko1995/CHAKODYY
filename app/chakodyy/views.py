from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated
from chakodyy.serializers import UpdateUserInfo, TokenObtainSerializer, UpdatePasswordSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UpdateUserInfo(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Updated'}, status=status.HTTP_200_OK)

class CutomObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer


class ResetPasswordView(APIView):
    def post(self, request, format=None):
        serializer = UpdatePasswordSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Updated'}, status=status.HTTP_200_OK)