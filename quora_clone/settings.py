import os
from pathlib import Path
from dotenv import  load_dotenv
load_dotenv()

BASE_DIR       = Path(__file__).resolve().parent.parent

SECRET_KEY      = os.getenv('SECRET_KEY')
DEBUG           = bool(os.getenv("LOCAL_DEBUG", default=0))
print(DEBUG)
ALLOWED_HOSTS   = []
SITE_ID         = 1
ALLOWED_HOSTS.extend(filter(None,os.getenv('ALLOWED_HOSTS','').split(','),))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.core',
    'widget_tweaks',
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

ROOT_URLCONF = 'quora_clone.urls'

TEMPLATES    = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS'    : [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'quora_clone.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME'  : BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE   = 'en-us'
TIME_ZONE       = 'UTC'
USE_I18N        = True
USE_TZ          = True


# Static files (CSS, JavaScript, Images)
STATIC_URL                = '/assets/'
STATICFILES_DIRS          = [os.path.join(BASE_DIR, "assets/"),]
MEDIA_URL                 = '/media/'
MEDIA_ROOT                = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT               = os.path.join(BASE_DIR, "files/")

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format'    : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt'   : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format'    : '%(levelname)s %(message)s'
        },
    },
    'handlers'  : {
        'file'  : {
            'level'     : 'DEBUG',
            'class'     : 'logging.FileHandler',
            'formatter' : 'verbose',
            'filename'  : "logs/errors.log",
        },
    },
    'loggers': {
        'django.request': {
            'handlers'  : ['file'],
            'level'     : 'DEBUG',
            'propagate' : True,
        },
        'api': {
            'handlers'  : ['file'],
            'level'     : 'DEBUG',
        }
    },
}
