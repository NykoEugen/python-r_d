from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from django.test import TestCase

from users.models import User


class UserModelTest(TestCase):
    def test_create_user(self):
        first_name = 'Rick'
        last_name = 'Moor'
        username = 'RickMoore'
        email = 'lolqwe@mail.com'
        password = 'Asdqwe123'
        user = User.objects.create_user(username=username, email=email, password=password,
                                        first_name=first_name, last_name=last_name)
        self.assertEquals(user.first_name, first_name)
        self.assertEquals(user.last_name, last_name)
        self.assertEquals(user.username, username)
        self.assertEquals(user.email, email)


class UserViewSetTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'test@mail.com',
            'password': 'testpasword',
            'first_name': 'Test1',
            'last_name': 'User1'
        }
        self.create_url = reverse('users:user-create')

    def test_create_user(self):
        response = self.client.post('/users/api/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_access_user(self):
        user = User.objects.create(username='testuser', first_name='Test', last_name='User')
        response = self.client.get(f'/users/api/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_delete_user(self):
        user = User.objects.create(username='testuser', first_name='Test', last_name='User')
        response = self.client.delete(f'/users/api/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
