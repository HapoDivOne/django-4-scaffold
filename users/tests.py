from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from django.urls import get_resolver
from django.test import Client

class UserAuthenticationTests(APITestCase):

    def setUp(self):
        self.username = 'duongh'
        self.password = 'admin123'
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user = get_user_model().objects.create_user(username=self.username, password=self.password)

    def test_login_with_valid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password,
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_with_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword',
        })

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', response.data)
        self.assertNotIn('refresh', response.data)

    def test_logout(self):
        # First, log in to get the refresh token
        login_response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password,
        })
        refresh_token = login_response.data['refresh']
        access_token = login_response.data['access']

    
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Bearer ' + access_token
        # Now, log out using the refresh token
        response = self.client.post(self.logout_url, {
            'refresh': refresh_token,
        })

        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
