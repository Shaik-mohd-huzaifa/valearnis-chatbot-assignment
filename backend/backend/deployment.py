import os
from .settings import *
from .settings import BASE_DIR

env = environ.Env(DEBUG=(bool, False))

environ.Env.read_env()

ALLOWED_HOSTS = [
    env(
        "WEBSITE_HOSTNAME",
        "https://valearns-chatapp-v1-epf8gwcndmavcufx.australiacentral-01.azurewebsites.net/",
    )
]

CSRF_TRUSTED_ORIGINS = [
    "https://"
    + env(
        "WEBSITE_HOSTNAME",
        "https://valearns-chatapp-v1-epf8gwcndmavcufx.australiacentral-01.azurewebsites.net/",
    )
]

DEBUG = False

SECRET_KEY = env("MY_SECRET_KEY", "4=ke^yg@lpb-po^&5hw5=&d0tr+usps==flhm%qoyeh!32*n8u")


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# CORS_ALLOWED_ORIGINS = []

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage. CompressedManifestStaticFilesStorage",
    },
}


STATIC_ROOT = BASE_DIR / "staticfiles"
