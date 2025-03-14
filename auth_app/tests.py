from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from auth_app.models import UserProfile

class RegisterTests(APITestCase):
    url = reverse('register')
    
    """
    Tests the correct registration.
    """
    def test_correct_registration(self):
        registration_data = {
            'email': 'test@peeet.net',
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
            'email': 'test@',
            'password': 'password123',
        }
        response = self.client.post(self.url, registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['details'], 'Please check your entries and try again.')

    """
    Tests missing registration data.
    """
    def test_missing_registration_data(self):
        registration_data = {
            'email': 'test@peeet.net'
        }
        response = self.client.post(self.url, registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['details'], 'Please check your entries and try again.')

    """
    Tests duplicate registration data.
    """
    def test_duplicate_registration(self):
        self.test_correct_registration()
        registration_data = {
            'email': 'test@peeet.net',
            'password': 'password123',
        }
        response = self.client.post(self.url, registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['details'], 'Please check your entries and try again.')


class LoginTests(APITestCase):
    pass


class ForgotPasswordTests(APITestCase):
    url = reverse('forgot-password')

    """
    Runs the correct registration test in order to have test user to work with.
    """
    def setUp(self):
        registration_data = {
            'email': 'test@peeet.net',
            'password': 'password123',
            'username': 'test'
        }
        UserProfile.objects.create_user(**registration_data)

    """
    Tests the correct forgot password request.
    """
    def test_correct_request(self):
        post_data = {'email': 'test@peeet.net'}
        response = self.client.post(self.url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['details'],
            'Please check your email for the password reset link.'
        )
    
    """
    Tests a bad forgot password request.
    """
    def test_bad_request(self):
        post_data = {'baaadrequest': 'badbadbad'}
        response = self.client.post(self.url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['details'],
            'Unable to process the request.'
        )

    """
    Tests the a forgot password request, where the user doesn't exist.
    """
    def test_user_not_existing_request(self):
        post_data = {'email': 'nonexistingemail@test.com'}
        response = self.client.post(self.url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['details'],
            'Unable to process the request.'
        )


class ResetPasswordTests(APITestCase):
    #url = reverse('reset-password')
    pass