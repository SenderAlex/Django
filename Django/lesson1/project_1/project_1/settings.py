"""
Django settings for project_1 project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os.path  # добавили эту библиотеку

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2pkw9%2-tti01%k^gv6r*fjv*in^n4$7v(@u@_9+^j+m^wn$_+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGIN = [
    'http://localhost',
    'http://127.0.0.1'
]
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost"
]  # добавили это. Configure Internal IPs

CSRF_COOKIE_SECURE = True

# DEBUG = False  # # это добавили 02.11.2023. Не работает без вписанных в ALLOWED_HOSTS = []
#
# ALLOWED_HOSTS = ['*']  # * означает, что ответ будет всем


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1.apps.App1Config',  # это добавили
    "debug_toolbar"  # это добавили
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware"  # это добавили
]

ROOT_URLCONF = 'project_1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #BASE_DIR / "templates"  # добавил как альтернатива нижней строки
            os.path.join(BASE_DIR, 'templates')  # что делает os.path.join -- оно берет путь который был и в конец
            # добавляет еще какую-то папочку. В данном случае BASE_DIR -- это папка проекта, а ее название в нашем случае "project_1"
        ],
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

WSGI_APPLICATION = 'project_1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

########################################################################
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',                       это я закоментировал
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
##########################################################################

# добавил эту базу
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Что делает этот метод? Коннектор с БД?
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
#############################################################################


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = 'items_admin'
