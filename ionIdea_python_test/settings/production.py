from utils import get_version
from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = []

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

STATIC_URL = "/static{}/".format(get_version(False))
STATIC_ROOT = BASE_DIR + STATIC_URL

try:
    from .local import *
except:
    pass
