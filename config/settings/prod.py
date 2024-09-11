from .base import *

SECRET_KEY = config('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['localhost', 'venuetix.pro']

# DATABASES - @TODO ADD POSTGRES