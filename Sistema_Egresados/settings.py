import os
import dj_database_url  

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0a!batjnq50!m86gza^ubxvtp)64xb=6)fmv-nqg4r4_w1)$38'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'domain',
    'web',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Sistema_Egresados.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'web/template')],
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

WSGI_APPLICATION = 'Sistema_Egresados.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'egresadosutp_db',

        'USER': 'jorge',
        'PASSWORD': 'jorge97',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

db_from_env = dj_database_url.config(conn_max_age=500)  
DATABASES['default'].update(db_from_env) 

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  
STATIC_URL = '/static/'
<<<<<<< HEAD
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (  
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

=======
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'web/static/media')
>>>>>>> versiones

#Email settings 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sistema.egresados.utp@gmail.com'
EMAIL_HOST_PASSWORD = 'sistemasutp2017'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#sesion settings
SESSION_COOKIE_AGE = 300 
SESSION_EXPIRE_AT_BROWSER_CLOSE = True




