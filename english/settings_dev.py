from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k#w7@z$&huj&8ur^0z^x39ty$+=uk)o9c21zo7q8_bsvnnu%o('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers':False,

    'loggers':{
        'django':{
            'handlers':['console'],
            'level':'INFO',
        },

        'vocabulary':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },

    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },

    'formatters':{
        'dev':{
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"