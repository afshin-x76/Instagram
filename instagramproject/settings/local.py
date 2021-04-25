from .base import *


DEBUG = True

# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'static'

# # STATICFILES_DIRS = [
# #     BASE_DIR / 'static',
# # ]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS =[
    BASE_DIR / 'static',
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'