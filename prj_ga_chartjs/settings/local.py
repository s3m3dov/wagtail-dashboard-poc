# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # postgres_linux
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'prj_ga_chartjs',
        'USER': 'hikmat',
        'PASSWORD': 'intelcorei7',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'postgres_win': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testdb2',
        'USER': 'postgres',
        'PASSWORD': 'NoLimit2023',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'production': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ciba',
    },
}

#add you redis password if you set
#elery_broker_url_local = "redis://:REDIS_PASSWORD_HERE@REDIS_ADDRESS:REDIS_PORT"