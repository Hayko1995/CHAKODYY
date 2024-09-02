from django.urls import path
from coin.views import BuyCoin


urlpatterns = [
    path('buy', BuyCoin.as_view(), name='action')
]
