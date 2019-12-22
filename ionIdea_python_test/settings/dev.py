from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
LOCAL_DEV = True

try:
    from .local import *
except:
    pass
