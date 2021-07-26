"""
This is sample local_settings.py file
Your local Database and Redis settings will be stored in this file.
Edit this file due to your local settings and copy this file to settings folder.
`cd samples; cp sample_local_settings.py ../prj_ga_chartjs/settings/local_settings.py`
(For example: Khazar uses sqlite3 in his local environment for database settings. He should set his DATABASE settings for sqlite.)
"""

#add you redis password if you set
celery_broker_url_local = "redis://:REDIS_PASSWORD_HERE@REDIS_ADDRESS:REDIS_PORT"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


#YOUR LOCAL DATABASE SETTINGS HERE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'prj_ga_chartjs',
        'USER': 'hikmat',
        'PASSWORD': 'intelcorei7',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}