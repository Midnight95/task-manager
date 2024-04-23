from django.test import TestCase
import json


class UserTestCase(TestCase):
    fixtures = ['users']

    with open('task_manager/fixtures/users_data.json') as file:
        test_data = json.loads(file.read())
