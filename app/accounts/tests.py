from django.test import TestCase
from rest_framework.test import APITestCase
from accounts.models import User
from django.urls import reverse
from rest_framework import status
import json
from django.contrib.auth import get_user_model
