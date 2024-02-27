from datetime import timedelta

from .base import *  # noqa
from .base import env

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

ADMIN_URL = env.str("ADMIN_URL", default="admin/")
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT", "Bearer"),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
}

# Email settings
# ----------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Stripe settings
STRIPE_PUBLISHABLE_KEY = env.str("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = env.str("STRIPE_SECRET_KEY")
STRIPE_API_VERSION = env.str("STRIPE_API_VERSION")
STRIPE_WEBHOOK_SECRET = env.str("STRIPE_WEBHOOK_SECRET")

# Channels
# ----------------------------------------------------------------
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}
