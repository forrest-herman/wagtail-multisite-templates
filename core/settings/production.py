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

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

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

# AWS_STORAGE_BUCKET_NAME = "atomic-waas"
# AWS_ACCESS_KEY_ID = "Q6V3HFYPTMJBNQHHSEGP"
# AWS_SECRET_ACCESS_KEY = "nhgIhyfyOpNGX+tkaAFx8/WLnEYsvRzK/ATYwm4wcAw"
# AWS_S3_CUSTOM_DOMAIN = "%s.nyc3.digitaloceanspaces.com" % AWS_STORAGE_BUCKET_NAME

# MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN


# S3 Bucket settings
AWS_ACCESS_KEY_ID = "Q6V3HFYPTMJBNQHHSEGP"
AWS_SECRET_ACCESS_KEY = "nhgIhyfyOpNGX+tkaAFx8/WLnEYsvRzK/ATYwm4wcAw"
AWS_STORAGE_BUCKET_NAME = "atomic-waas"
AWS_S3_ENDPOINT_URL = "https://nyc3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "ACL": "public-read",
    "CacheControl": "max-age=86400",
}
AWS_LOCATION = "atomic-waas"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# STATIC_URL = "https://%s/%s/" % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
# STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
MEDIA_URL = "https://atomic-waas.nyc3.digitaloceanspaces.com/"

# MEDIA_ROOT = "https://atomic-waas.nyc3.digitaloceanspaces.com"
# MEDIA_URL = "/media/"

try:
    from .local import *
except ImportError:
    pass
