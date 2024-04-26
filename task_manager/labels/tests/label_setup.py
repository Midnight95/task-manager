from django.test import TestCase, modify_settings
import json


@modify_settings(
    MIDDLEWARE={
        'remove': 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    }
)
class LabelTestCase(TestCase):
    fixtures = ['users', 'labels']

    with open('task_manager/fixtures/labels_data.json') as file:
        label_data = json.loads(file.read())
