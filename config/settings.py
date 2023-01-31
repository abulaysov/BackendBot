"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import json
import os
from pathlib import Path

import rest_framework.permissions

from djoser.constants import Messages
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv("DEBUG"))

CSRF_TRUSTED_ORIGINS = [
    "https://horaro.net",
    "https://www.horaro.net",
    "https://api.horaro.net",
    "https://www.api.horaro.net",
    "https://staging.horaro.net",
    "https://api.staging.horaro.net",
    "https://www.api.staging.horaro.net",
]

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "rest_framework",
    "corsheaders",
    "rest_framework.authtoken",
    "djoser",
    "drf_yasg",
    "api.apps.ApiConfig",
    "users.apps.UsersConfig",
    "bots.apps.BotsConfig",
    "django_filters",
]
SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "config.urls"

CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_ORIGINS = [
#     "https://horaro.net",
#     "https://api.horaro.net",
# ]


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

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "django.template.context_processors.media"
)

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_NAME"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en-us", "English"),
    ("ru", "Russian"),
)
TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "reset_password/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {
        "user_create": "users.serializers.RegisterCustomUserSerializer",
        "token": "users.serializers.TokenSerializer",
        "password_reset": "users.serializers.CustomSendEmailResetSerializer",
    },
    "PERMISSIONS": {
        "activation": ["rest_framework.permissions.AllowAny"],
        "password_reset": ["rest_framework.permissions.AllowAny"],
        "password_reset_confirm": ["rest_framework.permissions.AllowAny"],
        "set_password": ["djoser.permissions.CurrentUserOrAdmin"],
        "username_reset": ["rest_framework.permissions.AllowAny"],
        "username_reset_confirm": ["rest_framework.permissions.AllowAny"],
        "set_username": ["djoser.permissions.CurrentUserOrAdmin"],
        "user_create": ["rest_framework.permissions.AllowAny"],
        "user_delete": ["djoser.permissions.CurrentUserOrAdmin"],
        "user": ["djoser.permissions.CurrentUserOrAdminOrReadOnly"],
        "user_list": ["rest_framework.permissions.IsAdminUser"],
        "token_create": ["rest_framework.permissions.AllowAny"],
        "token_destroy": ["rest_framework.permissions.IsAuthenticated"],
    },
    "EMAIL": {
        "password_reset": "users.helpers.CustomPasswordResetEmail",
        "activation": "users.helpers.CustomActivationEmail",
    },
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "basic": {"type": "basic"},
        "Token": {"type": "apiKey", "in": "header", "name": "Authorization"},
    },
}


Messages.INVALID_CREDENTIALS_ERROR = "Вы ввели неправильный логин или пароль!"
Messages.INVALID_PASSWORD_ERROR = "Введен не правильный пароль."

LOGOUT_REDIRECT_URL = "/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

AUTH_USER_MODEL = "users.CustomUser"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")


CELERY_BROKER_URL = "redis://redis:6379/0"


if DEBUG:
    API_URL_TELEGRAM = os.getenv("TOKEN_BOT_STAGING")
else:
    API_URL_TELEGRAM = os.getenv("TOKEN_BOT_PROD")

with open("messages.json") as messages:
    MESSAGES = json.loads(messages.read())

