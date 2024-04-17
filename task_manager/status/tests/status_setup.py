from django.test import TestCase
import json


class StatusTestCase(TestCase):
    fixtures = ['user_objects', 'status_objects']

    with open('task_manager/fixtures/status_test_data.json') as file:
        test_data = json.loads(file.read())