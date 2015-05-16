from base import *

DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sigp-prod',
        'USER': 'juahni',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)

#STATIC_ROOT = '/home/juahni/PycharmProjects/sigp/sigp/'
staticos_prod = Path(__file__).ancestor(5)
STATIC_ROOT = staticos_prod.child('static')

MEDIA_URL = '/media/'

media_prod = Path(__file__).ancestor(5)
MEDIA_ROOT = media_prod.child('media')