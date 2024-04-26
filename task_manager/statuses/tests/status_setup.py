from django.test import TestCase, modify_settings
import json


@modify_settings(
    MIDDLEWARE={
        'remove': 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    }
)
class StatusTestCase(TestCase):
    fixtures = ['users', 'statuses']

    with open('task_manager/fixtures/statuses_data.json') as file:
        status_data = json.loads(file.read())
