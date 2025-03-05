from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class RegisterTests(APITestCase):
    url = reverse('register')
    
    """
    Tests the correct registration.
    """
    def test_correct_registration(self):
        registration_data = {
            'email': 'test@mail.com',
            'password': 'password123',
        }
        response = self.client.post(self.url, registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], registration_data['email'])

    def test_wrong_registration(self):
        # Test an invalid email field.
        pass

    def test_duplicate_registration(self):
        # Test what happens, when user already exists.
        pass