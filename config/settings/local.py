from .base import *

from dotenv import load_dotenv
from os import getenv, path

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)

SITE_NAME = getenv("SITE_NAME")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY", "django-insecure-&bhh4!zf3^(0g*#1k!r#(s#)n@(48#=^xrglbu2a!bs221ken$")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG", True)

ALLOWED_HOSTS = getenv("ALLOWED_HOSTS").split(",")

ADMIN_URL = getenv("ADMIN_URL", "admin")

CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8080", 
                        "http://localhost:8080",
                  
                        ]
CSRF_ALLOWED_ORIGINS = ["http://localhost:8080", 
                        "http://127.0.0.1:8080",
                       ]

CORS_ORIGINS_WHITELIST = ["http://127.0.0.1:8080"]


EMAIL_BACKEND = getenv('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_PORT = getenv('EMAIL_PORT')
EMAIL_USE_TLS = getenv('EMAIL_USE_TLS', default=True)
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = getenv('DEFAULT_FROM_EMAIL')



LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}