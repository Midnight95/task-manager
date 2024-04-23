from django.test import TestCase
import json


class StatusTestCase(TestCase):
    fixtures = ['users', 'statuses']

    with open('task_manager/fixtures/statuses_data.json') as file:
        status_data = json.loads(file.read())
