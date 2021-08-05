"""
This is sample local_settings.py file
Your local Database and Redis settings will be stored in this file.
Edit this file due to your local settings and copy this file to settings folder.
`cd samples; cp sample_local_settings.py ../prj_ga_chartjs/settings/local_settings.py`
(For example: Khazar uses sqlite3 in his local environment for database settings. He should set his DATABASE settings for sqlite.)
"""

import os
from pathlib import Path

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / 'templates'

#set env to get password
redis_secret = os.environ.get("redis_secret")
celery_broker_url_local = f"redis://:{redis_secret}@127.0.0.1:6379"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#YOUR LOCAL DATABASE SETTINGS HERE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
