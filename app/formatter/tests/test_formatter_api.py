from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


FORMAT_QUERY_URL = reverse('formatter:format')

class FormatAPITestCase(APITestCase):

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

