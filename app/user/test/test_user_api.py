from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

CREATE_USER_URL = reverse('user:create')
#CREATE_TOKEN_URL = reverse('user:token')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class APITESTCASE(APITestCase):
    def test_creating_user(self):
        payload = {
            'username': 'testuser',
            'password': 'testpass123',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_creating_existing_user(self):
        payload = {
            'username': 'testuser',
            'password': 'testpass123',
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

