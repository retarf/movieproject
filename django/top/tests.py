from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class CommentTestCase(APITestCase):
    def test_get_request(self):
        url = reverse('top:index')
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))
