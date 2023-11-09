"""
Django settings for ProyectoFinal project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

from django.contrib.messages import constants as mensajes_de_error

import ProyectoFinal.config as config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wqk%(e0g0=h^20g^(n$ay&0ry$iv+q6eprq*2dzxyl0p61!n03'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#STATICFILES_DIRS = ['D:/ウサク/2022/Segundo Semestre/Proyectos de computación/Proyecto/Proyecto Final/ProyectoFinal/Templates/static']

# Application definition

INSTALLED_APPS = [
    # 'jet_django',
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #My apps
    'profesor',
    'stock',
    'cursos',
    #'inventario',
    'carro',
    'autenticacion',
    'pedidos',
    'reconocimiento',
    # 'user',
    'usuarios',
    # Librerias
    'crispy_forms',
    'axes',
    'import_export',
    'crispy_bootstrap4',
    
]

JAZZMIN_UI_TWEAKS = {
    # "theme": "cosmo",
     "theme": "flatly",
    #"theme": "litera",
}

JAZZMIN_SETTINGS = {
    "site_title": "Music Academy",
    "site_header": "Music Academy",
    "site_logo": "admin/logo5.png",
    "login_logo": None,
    "site_icon": None,
    "user_avatar": "admin/logo5.png",

}


AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesStandaloneBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'axes.middleware.FailedLoginMiddleware',
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'ProyectoFinal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
       'DIRS': [os.path.join(BASE_DIR, 'Templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carro.context_processor.importe_total_carro',
            ],
        },
    },
]

WSGI_APPLICATION = 'ProyectoFinal.wsgi.application'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = config.DATABASES

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '123456789aQ+',
#         'HOST': 'academia.csmvs9rxjugb.us-east-2.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
    {   'NAME': 'ProyectoFinal.validators.UppercaseValidator', 
    },
    {   'NAME': 'ProyectoFinal.validators.DigitValidator', 
    },
    {   'NAME': 'ProyectoFinal.validators.SymbolValidator', 
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-eu'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR /'staticfiles'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "musicacademy997@gmail.com"        #####Correo desde el que se enviaran los correos, tambien corregir en autenticacion > views > enviar_correo
EMAIL_HOST_PASSWORD = "bdpt xcpb cbix njdd"                 #####Clave generada en el correo

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK='bootstrap4'

MESSAGE_TAGS = {

    mensajes_de_error.DEBUG: 'debug',
    mensajes_de_error.INFO: 'info',
    mensajes_de_error.SUCCESS: 'success',
    mensajes_de_error.WARNING: 'warning',
    mensajes_de_error.ERROR: 'danger',

}

AXES_FAILURE_LIMIT = 5
AXES_LOCKOUT_CALLABLE = "autenticacion.views.lockout"
AXES_ONLY_USER_FAILURES	= True
AUTH_USER_MODEL = 'auth.User'

#AUTH_USER_MODEL='user.User'