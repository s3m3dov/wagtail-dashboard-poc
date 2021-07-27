from .base import *
from .dev import SECRET_KEY

DEBUG = False
ALLOWED_HOSTS = ['*'] 

try:
    from .local import *
except ImportError:
    pass
