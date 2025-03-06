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

    """
    Tests wrong registration data.
    """
    def test_wrong_registration(self):
        registration_data = {
            'email': 'test@mail',
            'password': 'password123',
        }
        response = self.client.post(self.url, registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Please check your entries and try again.')

    """
    Tests missing registration data.
    """
    def test_missing_registration_data(self):
        registration_data = {
            'email': 'test@mail'
        }
        response = self.client.post(self.url, registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Please check your entries and try again.')

    """
    Tests duplicate registration data.
    """
    def test_duplicate_registration(self):
        self.test_correct_registration()
        registration_data = {
            'email': 'test@mail.com',
            'password': 'password123',
        }
        response = self.client.post(self.url, registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Please check your entries and try again.')