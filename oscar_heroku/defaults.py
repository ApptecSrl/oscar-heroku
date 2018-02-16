from .utils import getenv

SITE_ID = 1


AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}


OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

GOOGLE_ANALYTICS_ID = getenv('GOOGLE_ANALYTICS_ID', None)

DEFAULT_FROM_MAIL = SERVER_EMAIL = getenv('DEFAULT_FROM_MAIL', 'superuser@example.com')

OSCAR_FROM_EMAIL = getenv('DEFAULT_FROM_MAIL', 'superuser@example.com')


USE_S3 = True if getenv('USE_S3', 'False') == 'True' else False


if USE_S3:
    AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }
    AWS_STORAGE_BUCKET_NAME = getenv('AWS_STORAGE_BUCKET_NAME', '')
    AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY', '')
    AWS_IS_GZIPPED = True

    # Tell django-storages that when coming up with the URL for an item in S3
    # storage, keep it simple - just use this domain plus the path.
    # (If this isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets expanded,
    # if you're using it.
    # We also use it in the next setting.
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATIC_URL = "https://%s/static/" % AWS_S3_CUSTOM_DOMAIN
    COMPRESS_URL = "https://%s/static/" % AWS_S3_CUSTOM_DOMAIN
    MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN

    STATICFILES_STORAGE = 'oscar_heroku.s3utils.StaticRootS3BotoStorage'
    COMPRESS_STORAGE = 'oscar_heroku.s3utils.StaticRootS3BotoStorage'
    DEFAULT_FILE_STORAGE = 'oscar_heroku.s3utils.MediaRootS3BotoStorage'



LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
        'simple': {
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        # Django loggers
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'sentry'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.security': {
            'handlers': ['mail_admins', 'sentry'],
            'propagate': False,
            'level': 'WARNING',
        },
        # Oscar core loggers
        'oscar.checkout': {
            'handlers': ['console', 'sentry'],
            'propagate': False,
            'level': 'INFO',
        },
        'oscar.catalogue.import': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        },
        'commands': {
            'handlers': ['console', 'sentry'],
            'propagate': False,
            'level': 'INFO',
        },
        'oscar.alerts': {
            'handlers': ['mail_admins', 'sentry'],
            'propagate': False,
            'level': 'INFO',
        },
        # Sandbox logging
        'gateway': {
            'handlers': ['sentry'],
            'propagate': True,
            'level': 'INFO',
        },
        # Third party
        'sorl.thumbnail': {
            'handlers': ['sentry'],
            'propagate': True,
            'level': 'INFO',
        },
        # Suppress output of this debug toolbar panel
        'template_timings_panel': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'paypal.express': {
            'handlers': ['console', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
