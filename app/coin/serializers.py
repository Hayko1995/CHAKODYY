from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from coin.models import CoinCount, CoinName
import json
from blog.models import Actions, Projects, Groups, Roles
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


class BuyCoinSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    count = serializers.FloatField(required=True)

    class Meta:
        model = CoinCount
        fields = ["name", "count"]
        required_fields = fields

    def create(self, attrs):
        try:
            coin_name = CoinName.objects.filter(name=attrs["name"]).first()

            if not coin_name:
                coin_name = CoinName.objects.create(name=attrs["name"])
                coin_name.save()

            coin_count = CoinCount.objects.filter(name__in=[coin_name]).first()

            if not coin_count:
                coin_count = CoinCount.objects.create(
                    name=coin_name, count=attrs["count"], times=[datetime.now()]
                )
                coin_count.save()
            else:
                coin_count.count = coin_count.count + attrs["count"]
                coin_count.times.append(datetime.now())
                coin_count.save()
            
            

        except Exception as e:
            # todo add logging
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_200_OK)
