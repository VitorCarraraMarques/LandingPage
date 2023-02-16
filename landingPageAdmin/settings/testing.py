from .settings import *

DEBUG = True 

SECRET_KEY = '@^*$*%ns2+@bc4bepomdp8u0ogcn1oqkwu4@3ndxpx4f1g0%y6' 

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}