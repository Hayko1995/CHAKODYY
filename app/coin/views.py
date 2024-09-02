from django.shortcuts import render
from rest_framework.views import APIView

from coin.serializers import (
    BuyCoinSerializer,

)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


class BuyCoin(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        print(request)
        print("🐍 File: coin/views.py | Line: 18 | post ~ request",request.user)
        serializer = BuyCoinSerializer(
            data=request.data, context={"user": request.user}
        )
        results = serializer.create(request.data)
        return results