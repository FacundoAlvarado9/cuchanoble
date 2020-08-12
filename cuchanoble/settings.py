import os
from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)


ALLOWED_HOSTS = ['localhost', '127.0.0.1', '104.236.5.15', 'cuchanoble.org']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'perros',

    #Autenticacion
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',

    'rest_auth',

    #Author
    'author',

    #FormTweaks
    'widget_tweaks',

    #Django rest
    'rest_framework',
    'rest_framework.authtoken',

    #AWS S3 packages
    'storages',
]

# Rest framwork - autenticacion
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'author.middlewares.AuthorDefaultBackendMiddleware',
]

ROOT_URLCONF = 'cuchanoble.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #UBicacion de los templates html
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cuchanoble.wsgi.application'


default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

# DATABASES = {
#     'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
#  }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'db_user',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'America/Argentina/Rio_Gallegos'

USE_I18N = True

USE_L10N = True

USE_TZ = True

################## AWS S3 #############################

#Estableciendo parametros
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_UPLOAD_GROUP = config('AWS_UPLOAD_GROUP')
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com'
AWS_QUERYSTRING_AUTH = False
S3DIRECT_REGION = 'sa-east-1'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = 'staticfiles'
# Nueva URL de archivos estaticos
# STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.' + 's3.amazonaws.com/'
STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
# STATIC_URL = '/static/'

#nueva URL de archivos media
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = STATIC_URL + 'media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static/"),
)

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

################### AUTENTICACION ########################

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# A donde me lleva la pagina luego de...
LOGIN_REDIRECT_URL = "/subir/"
SIGNUP_REDIRECT_URL = "/subir/"

#Estableciendo prioridad de email en lugar de nombre de usuario
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# Eliminando paso intermedio al cerrar sesion
ACCOUNT_LOGOUT_ON_GET =  True
LOGIN_REDIRECT_URL = '/perros/subir/'
ACCOUNT_EMAIL_VERIFICATION = 'None'

#Formulario personalizado de registro
ACCOUNT_SIGNUP_FORM_CLASS = 'perros.forms.SignupForm'


SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        #'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.5',
    }
}
