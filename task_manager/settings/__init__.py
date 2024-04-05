import os

STAGE = os.environ.get('APP_STAGE', 'dev')
if STAGE == 'prod':
    from .prod import  *
else:
    from .dev import *
