from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from unittest import mock
from formatter.views import llm_format

FORMAT_QUERY_URL = reverse('formatter:formatter')

def create_user(username='tester', password='testpass123'):
    return get_user_model().objects.create_user(username=username,password=password)

class FormatAPITestCase(APITestCase):

    def setUp(self):
        self.user = create_user()
        self.client.force_authenticate(user=self.user)

    def test_creating_query(self):
        payload = {
            'raw_Query': "select a.id,b.name from users a join user_profiles b on a.id=b.user_id where a.status='active'and b.country='USA';"
        }
        res = self.client.post(FORMAT_QUERY_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_empty_query(self):
        payload = {}
        res = self.client.post(FORMAT_QUERY_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    @mock.patch('formatter.views.llm_format')
    def test_format_query(self, mock_llm_format):
        payload = {
            'raw_Query': "SeLEct   name,AGE,email  FrOm   USERS   wHeRe age>20   and   Email LIKE '%@example.com'order BY   age  DESC ;"
        }
        formatted_query = "SELECT \n    name,\n    AGE,\n    email\nFROM \n    USERS\nWHERE \n    age > 20 \nAND \n    Email LIKE '%@example.com'\nORDER BY \n    age DESC;"

        mock_llm_format.return_value = formatted_query

        res = self.client.post(FORMAT_QUERY_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['formatted_Query'], formatted_query)
