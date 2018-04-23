import os
import dj_database_url
from django.utils.log import DEFAULT_LOGGING
import datetime
from utils.jwt import jwt_response_payload_handler

DEFAULT_LOGGING['handlers']['console']['filters'] = []
# IS ON PRODUCTION?
def is_on_production_environment():
    is_production = os.getenv('LNPOINT_ENVIRONMENT', 'development')
    return is_production == 'production'


IS_ON_PRODUCTION_ENVIRONMENT = is_on_production_environment()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'n3wS3Cr37k3Y!1!!11f0Rle4RNp01n7!!11!!^&^@@$SDBcag@$@$'

if IS_ON_PRODUCTION_ENVIRONMENT:
    SESSION_COOKIE_DOMAIN = '.lnpoint.com'
SESSION_COOKIE_NAME = 'learnpoint_sessid'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if IS_ON_PRODUCTION_ENVIRONMENT else True

# Redirect HTTPS
if IS_ON_PRODUCTION_ENVIRONMENT:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['localhost',
                 'lp-rose.herokuapp.com',
                 'lnpoint.com', 'www.lnpoint.com']

# Application definition

INSTALLED_APPS = [
    #Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Package Apps
    'django_mobile',
    'storages',
    'rest_framework',
    #Project Apps
    'accounts',
    'kelas',
    'profiles',
    'usermessages',
    'activity',
]


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',

)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_ALLOW_REFRESH': True,
    'JWT_RESPONSE_PAYLOAD_HANDLER': jwt_response_payload_handler
}

ROOT_URLCONF = 'learnpoint.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_mobile.context_processors.flavour',
            ],
        },
    },
]

TEMPLATE_LOADERS = ['django_mobile.loader.Loader',]

WSGI_APPLICATION = 'learnpoint.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
                default='sqlite:///{0}'.format(location('db.sqlite3')),
                conn_max_age=500)
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# STATIC (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'assets'),]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')
STATIC_URL = STATIC_HOST + '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CACHES
if IS_ON_PRODUCTION_ENVIRONMENT:
    CACHES = {
        'default': {
            'BACKEND': 'django_bmemcached.memcached.BMemcached',
            'LOCATION': os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','),
            'OPTIONS': {
                        'username': os.environ.get('MEMCACHEDCLOUD_USERNAME'),
                        'password': os.environ.get('MEMCACHEDCLOUD_PASSWORD')
                }
        }
    }

# MEDIA
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_SECURE_URLS = True
AWS_QUERYSTRING_AUTH = False
AWS_S3_ACCESS_KEY_ID = 'AKIAIB7R7B5RNQH5RRQQ'
AWS_S3_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'lnpoint-media'
AWS_S3_CUSTOM_DOMAIN = 'd2wefhtvovcf6q.cloudfront.net'

# AUTH
AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = '/accounts/login/'
LOGIN_URL = '/accounts/login/'

# EMAIL
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'dev@lnpoint.id')

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'question_suggestion')

# TWILIO
TWILIO_ACCOUNT_SID = 'ACa62fe99f7b482db3d7a8bf438f8320ac'
TWILIO_AUTH_TOKEN = '6e96afad8a999b2ff6cad971d3b415ba'
TWILIO_FROM = '+16788837888'
