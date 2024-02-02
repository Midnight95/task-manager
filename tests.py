from django.test import TestCase, Client
from task_manager.user.models import User

class TestUser(TestCase):
    @classmethod
    def setUp():
        cls.client = Client()
        cls.credentials = {
            'username': 'user',
            'password': 'password1'
        }

        cls.user = User.objects.create(**cls.credentials)



