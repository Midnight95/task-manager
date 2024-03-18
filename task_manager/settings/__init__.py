import os

STAGE = os.environ.get('APP_STAGE', 'dev')
if STAGE == 'prod':
    from .prod import *  #noqa F403
else:
    from .dev import *  #noqa F403
