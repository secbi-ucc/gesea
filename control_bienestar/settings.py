"""
Django settings for control_bienestar project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$0x_kqva!@jl024f$n^t9dxn_j#-#%vg7=g=gk!lfr7na+o#j='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True




# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'actividades',
    'profesor',
    'programacion',
    'core',
    'inscripcion',
    'import_export',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

SUIT_CONFIG  =  {
    'ADMIN_NAME': 'CONTROL BIENESTAR',
    'SEARCH_URL' :  '',
    'LIST_PER_PAGE' :  50 ,
    'MENU_ICONS': {
        'actividades': ' icon-folder-open',
        'auth': 'icon-lock',
        'inscripcion':' icon-list-alt',
        'profesor':' icon-user',
        'programacion':'icon-calendar',
    }


}



ROOT_URLCONF = 'control_bienestar.urls'

LOGIN_REDIRECT_URL = '/admin'

WSGI_APPLICATION = 'control_bienestar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join("core/templates"),
    # here you can add another templates directory if you wish.
)

# Static files (CSS, JavaScript, Images)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATICFILES_DIRS = (
    os.path.join('core/static'),
)

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
# https://docs.djangoproject.com/en/1.7/howto/static-files/


MEDIA_URL = '/media/'

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
