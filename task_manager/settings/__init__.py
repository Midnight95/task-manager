import os

STAGE = os.environ.get('APP_STAGE', 'dev')
if STAGE == 'prod':
    from .production import *
else:
    from .development import *
