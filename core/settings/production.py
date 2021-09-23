from typing import Tuple
from .base import *
import os

env = os.environ.copy()
SECRET_KEY = env["SECRET_KEY"]

# Parse database configuration from $DATABASE_URL
import dj_database_url

DATABASES["default"] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
]
COMPRESS_CSS_HASHING_METHOD = "content"


# Allow all host headers
ALLOWED_HOSTS = ["*"]

# DEBUG = False
DEBUG = True

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
MEDIA_URL = "/media/"

try:
    from .local import *
except ImportError:
    pass
