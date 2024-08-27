"""chakodyy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from chakodyy.token import CustomJWTToken
from chakodyy.oauth.google import ObtainUserFromGoogle

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from accounts.models import User
from chakodyy.views import UserChangePasswordView, CutomObtainPairView, ResetPasswordView
from rest_framework_simplejwt.views import TokenBlacklistView
from two_factor.urls import urlpatterns as tf_urls
from accounts.admin import admin_site
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Original Admin panel
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('blog/', include('blog.urls')),

    # URLs for Djoser/Django social OAuth2 login.
    path('api/auth/social/', include('djoser.social.urls')),
    path('api/auth/social_django/',
         include('social_django.urls', namespace='social')),
    path('accounts/profile/', ObtainUserFromGoogle.as_view()),
    path('api/auth/', include('djoser.urls.jwt')),

    path('api/auth/jwt/create', CustomJWTToken.as_view(), name='login'),
    path('updateUser/', UserChangePasswordView.as_view(), name='updateUser'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path('auth/jwt/create/', CutomObtainPairView.as_view(), name='login'),
    path('resetPassword/', ResetPasswordView.as_view(), name='customtoken'),

    path('otp/', admin_site.urls),

    
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
