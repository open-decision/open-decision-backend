"""
Django settings for opendecision project.
Generated by 'django-admin startproject' using Django 2.2.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
from .ckeditor_settings import *
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = (os.path.join(
    BASE_DIR, "opendecision", "static"),)
STATIC_ROOT = os.path.join(
    BASE_DIR, "production", "collected_static")
MEDIA_ROOT = os.path.join(BASE_DIR, "production", "media")

# Heroku Settings
if os.environ.get('HEROKU') is not None:
    ALLOWED_HOSTS = ['.herokuapp.com']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    # Heroku: Update database configuration from $DATABASE_URL.
    import dj_database_url
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)

    STATIC_URL = f'{BASE_DIR}/production/collected_static/'
    CKEDITOR_BASEPATH = f'{STATIC_URL}ckeditor/ckeditor/'

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

#Azure Settings
elif os.environ.get('AZURE') is not None:
    ALLOWED_HOSTS = [
        '.open-decision.org',
        'open-decision.azureedge.net',
        'od-prod.azurewebsites.net',
        'od-prod-od-staging.azurewebsites.net',
        'od-static.azureedge.net',
        '127.0.0.1'
    ]

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': os.environ.get('DATABASE_PORT', ''),
        'OPTIONS': {
            'sslmode': 'require',
        }
    }
}
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    DEFAULT_FILE_STORAGE = 'opendecision.custom_azure.AzureMediaStorage'
    STATICFILES_STORAGE = 'opendecision.custom_azure.AzureStaticStorage'

    STATIC_LOCATION = "static"
    MEDIA_LOCATION = "media"

    AZURE_ACCOUNT_NAME = os.environ.get('STORAGE_ACCOUNT_NAME')
    AZURE_CUSTOM_DOMAIN = 'od-static.azureedge.net'
    STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
    CKEDITOR_BASEPATH = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/ckeditor/ckeditor/'

if os.environ.get('DJANGO_PRODUCTION') is not None:

    # SECURITY
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

    #SECURE_SSL_REDIRECT = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_HSTS_SECONDS = 30
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    #SECURE_HSTS_PRELOAD = True
    SECURE_REFERRER_POLICY = 'None'
    #TODO review later
    # CSRF_COOKIE_SECURE = True
    # SESSION_COOKIE_SECURE = True


    if os.environ.get('SMTP_SERVER') is not None:
        # E-Mail configuration
        EMAIL_HOST = os.environ.get('SMTP_SERVER')
        EMAIL_PORT = 587
        EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
        EMAIL_USE_TLS = True

        # Sender mails
        SERVER_EMAIL = os.environ.get('SERVER_EMAIL')
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

    # Admin  configuration
    ADMINS = [(os.environ.get('ADMIN1_NAME'), os.environ.get('ADMIN1_EMAIL'))]

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',

        'ckeditor',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'django_inlinecss',
        'storages',
        'graphene_django',
        'corsheaders',
        'graphql_auth',
        'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
        'django_filters',

        'users',
        'pages',
        'builder',
        'dashboard',
        'api',
        'visualbuilder',
    ]
    API_TEST_USER_MAIL = os.environ.get('API_TEST_USER_MAIL')

else:
    DEBUG = True
    CORS_ORIGIN_ALLOW_ALL = DEBUG
    CKEDITOR_BASEPATH = "/opendecision/static/ckeditor/ckeditor/"
    STATIC_URL = '/opendecision/static/'
    SECRET_KEY = '678&exk6aus^#z8j+#tco4%_bgv6mvd6!kcf!gokhza$)3sjql'
    API_TEST_USER_MAIL = os.environ.get('API_TEST_USER_MAIL', 'test@open-decision.org')
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',

        'ckeditor',
        'debug_toolbar',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'django_inlinecss',
        'graphene_django',
        'corsheaders',
        'graphql_auth',
        'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
        'django_filters',


        'users',
        'pages',
        'builder',
        'dashboard',
        'api',
        'visualbuilder',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    ACCOUNT_EMAIL_VERIFICATION = "none"
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



ROOT_URLCONF = 'opendecision.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR), 'templates'],
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

WSGI_APPLICATION = 'opendecision.wsgi.application'

GRAPHENE = {
    'SCHEMA': 'opendecision.schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'users.CustomUser'
AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend',
     "graphql_auth.backends.GraphQLAuthBackend",

)
SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
LOGIN_REDIRECT_URL = '/dashboard/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/logout-redirect'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Open Decision - '

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# LANGUAGES = (
#     ('en', _('English')),
#     ('de', _('German')),
# )

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

INTERNAL_IPS = [
    '127.0.0.1',
]

LOCALE_PATHS = [
os.path.join(
    BASE_DIR, "locale"),
]

# Custom Data for Open Decision
DATAFORMAT_VERSION = 0.1
LOGIC_TYPE = 'jsonLogic'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://localhost:3000',
    'http://127.0.0.1:3000',
    'https://127.0.0.1:3000',
    ]

if os.environ.get('CORS_ALLOWED'):
    for origin in os.environ.get('CORS_ALLOWED').split(','):
        CORS_ALLOWED_ORIGINS.append(origin.strip())

CORS_ALLOW_CREDENTIALS = True


GRAPHQL_JWT = {

    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,

    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ResendActivationEmail",
        "graphql_auth.mutations.SendPasswordResetEmail",
        "graphql_auth.mutations.PasswordReset",
        "graphql_auth.mutations.ObtainJSONWebToken",
        "graphql_auth.mutations.VerifyToken",
        "graphql_auth.mutations.RefreshToken",
        "graphql_auth.mutations.RevokeToken",
        "graphql_auth.mutations.VerifySecondaryEmail",
    ],
}

if os.environ.get('JWT_COOKIE_SAMESITE'):
    GRAPHQL_JWT['JWT_COOKIE_SAMESITE'] = os.environ.get('JWT_COOKIE_SAMESITE')

if os.environ.get('JWT_COOKIE_SAMESITE') == 'None':
    GRAPHQL_JWT['JWT_COOKIE_SECURE'] = True

if os.environ.get('JWT_COOKIE_DOMAIN'):
    GRAPHQL_JWT['JWT_COOKIE_DOMAIN'] = os.environ.get('JWT_COOKIE_DOMAIN')
