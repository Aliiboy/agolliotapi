import os

from .base import *  # noqa: F403
from .base import BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.getenv("DB_NAME", ""),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = os.getenv("STATIC_URL", "")
STATIC_ROOT = BASE_DIR / os.getenv("STATIC_ROOT", "")
MEDIA_URL = os.getenv("MEDIA_URL", "")
MEDIA_ROOT = BASE_DIR / os.getenv("MEDIA_ROOT", "")

# django-compressor
COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT
