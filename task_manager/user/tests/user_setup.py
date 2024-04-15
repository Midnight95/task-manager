from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.user.models import User
import json


def load_data(path: str):
    with open(path) as file:
        return json.loads(file.read())


class UserTestCase(TestCase):
    fixtures = ['user_objects']

    with open('task_manager/fixtures/user_test_data.json') as file:
        test_data = json.loads(file.read())