import os
from pathlib import Path
from decouple import config
import dj_database_url

"""
Django settings for tts project (Render deployment ready with SQLite + Whitenoise)
"""

# ----------------- PATHS -----------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------- SECURITY -----------------
SECRET_KEY = config('SECRET_KEY', default='django-insecure-ymj2bavyv&y=l$-o#oc95-!zvueijny@@3t8ronx=puo$38xwy')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['*']  # For Render & local

# ----------------- APPLICATIONS -----------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'core',
]

# ----------------- MIDDLEWARE -----------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ Static files handler for Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------- URL / WSGI -----------------
ROOT_URLCONF = 'tts.urls'
WSGI_APPLICATION = 'tts.wsgi.application'

# ----------------- TEMPLATES -----------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # global templates
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

# ----------------- DATABASE -----------------
# Local SQLite — stays within repo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------- PASSWORD VALIDATORS -----------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------- INTERNATIONALIZATION -----------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------- STATIC FILES -----------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # for dev
STATIC_ROOT = BASE_DIR / "staticfiles"     # for Render

# ✅ Whitenoise compressed static files storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ----------------- DEFAULT PK -----------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ----------------- RENDER-SPECIFIC -----------------
# Helps Render detect the environment correctly
if not DEBUG:
    import logging
    logging.basicConfig(level=logging.INFO)
    print("✅ Running in Render Production Mode with SQLite + Whitenoise")
