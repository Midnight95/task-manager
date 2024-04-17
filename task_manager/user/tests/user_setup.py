from django.test import TestCase
import json


class UserTestCase(TestCase):
    fixtures = ['user_objects']

    with open('task_manager/fixtures/user_test_data.json') as file:
        test_data = json.loads(file.read())
