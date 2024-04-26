from django.test import TestCase, modify_settings
import json


@modify_settings(
    MIDDLEWARE={
        'remove': 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    }
)
class UserTestCase(TestCase):
    fixtures = ['users']

    with open('task_manager/fixtures/users_data.json') as file:
        test_data = json.loads(file.read())
