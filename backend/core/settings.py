import os
from datetime import timedelta
from pathlib import Path

import environ
from dotenv import find_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
if DEBUG := env.bool("DEBUG", default=True):
    environ.Env.read_env(find_dotenv(".env"))

DEFAULT = "some_default_key"

SECRET_KEY = env.str("SECRET_KEY", default=DEFAULT)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=['*'])

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "api",
    "candidate",
    "users",
]

EXTERNAL_APPS = [
    "drf_yasg",
    "rest_framework",
    "djoser",
]

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + EXTERNAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": env.str("POSTGRES_ENGINE",
                          default='django.db.backends.postgresql'),
        "NAME": env.str("POSTGRES_NAME", default='postgres'),
        "USER": env.str("POSTGRES_USER", default='postgres'),
        "PASSWORD": env.str("POSTGRES_PASSWORD", default='postgres'),
        "HOST": env.str("POSTGRES_HOST", default='localhost'),
        "PORT": env.str("POSTGRES_PORT", default='5432'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'HIDE_USERS': True,
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL': 'api/v1/activate/{uid}/{token}',
    'SERIALIZERS': {
        'user_create': 'users.serializers.UserRegistrationSerializer',
        'user': 'users.serializers.UserSerializer',
        'current_user': 'users.serializers.UserSerializer',
    },
    'PERMISSIONS': {
        'user_list': ['rest_framework.permissions.IsAdminUser'],
    }
}

# EMAIL CONFIG
EMAIL_BACKEND = env.str("EMAIL_BACKEND",
                        default="django.core.mail.backends.smtp.EmailBackend")
EMAIL_HOST = env.str("EMAIL_HOST", default="smtp.yandex.ru")
EMAIL_PORT = env.str("EMAIL_PORT", default="465")
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="email_username")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="email_password")
EMAIL_USE_SSL = env.str("EMAIL_USE_SSL", default=True)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'api.v1.urls.api_info',
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = "media/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

RESUMES_UPLOAD = "resumes/"

RESUMES_ARCHIVE_FILENAME = "resumes.zip"

PHOTO_UPLOAD = "photo/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'users.User'
