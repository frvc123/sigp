from .base import *

DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bdproduccion',
        'USER': 'fran',
        'PASSWORD': 'fran02',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)

#STATIC_ROOT = '/home/daniel/dev/is2-env/static/'
staticos_prod = Path(__file__).ancestor(5)
STATIC_ROOT = staticos_prod.child('static')

ALLOWED_HOSTS = ['*']