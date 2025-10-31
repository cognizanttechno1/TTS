import os
from pathlib import Path
import dj_database_url
from decouple import config

"""
Django settings for tts project (Render deployment ready with SQLite).
"""

# ----------------- PATHS -----------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------- SECURITY -----------------
SECRET_KEY = config('SECRET_KEY', default='django-insecure-ymj2bavyv&y=l$-o#oc95-!zvueijny@@3t8ronx=puo$38xwy')
DEBUG = config('DEBUG', default=False, cast=bool)

# Allow Render and local access
ALLOWED_HOSTS = ['*']

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
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For serving static files on Render
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
        # Global templates folder
        'DIRS': [BASE_DIR / "templates"],
        # App-specific templates (e.g., core/templates/core/)
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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # SQLite stored in repo
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
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Enable Whitenoise compressed storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ----------------- DEFAULT PK -----------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
