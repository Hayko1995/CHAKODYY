from django.test import TestCase
from rest_framework.test import APITestCase
from accounts.models import User
from django.urls import reverse
from rest_framework import status
import json
from django.contrib.auth import get_user_model

User = get_user_model()

class APITest(APITestCase):
    try:
        self.user = User.objects.create_user(username='testuser', password='12345', email='example@gmail.com')  
    except:
        pass

    def testLogin(self):

        response = self.client.post('/auth/jwt/create/', data=json.dumps({"email": "example@gmail.com", "password": "Admin123!@#"}), content_type='application/json')

        self.client.post(
           '/auth/jwt/create/',
            {"email": "example@gmail.com", "password": "Admin123!@#"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data[username], 'username')
