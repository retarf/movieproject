from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status


class MovieTestCase(APITestCase):
    def test_url_root(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))

if __name__ == '__main__':
    unittest.main()
