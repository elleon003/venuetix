from .base import *

SECRET_KEY = 'django-insecure-moxv5mwt@a7i8xwkbsl@q-u3$bckf_pk-hfi1h4gn6xd4sdqod'
DEBUG = True
ALLOWED_HOSTS = ['alive-cleanly-flamingo.ngrok-free.app', '127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}