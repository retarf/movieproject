from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class MovieTestCase(APITestCase):
    def test_url_root(self):
        url = reverse('movies:index')
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))

    def test_post_request(self):
        url = reverse('movies:index')
        response = self.client.post(url, {'title': 'new idea'}, format='json')
        self.assertTrue(status.is_success(response.status_code))
