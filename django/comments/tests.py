from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class CommentTestCase(APITestCase):
    def test_get_request(self):
        url = reverse('comments:index')
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))

    def test_post_request(self):
        url = reverse('comments:index')
        response = self.client.post(url, {'movie_id': 1,"content": "test"}, format='json')
        self.assertTrue(status.is_success(response.status_code))
