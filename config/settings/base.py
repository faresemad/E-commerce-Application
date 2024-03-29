from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()


DJANGO_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "ckeditor",
    "djoser",
    "drf_spectacular",
    "django_filters",
]

LOCAL_APPS = [
    "apps.users",
    "apps.products",
    "apps.orders",
    "apps.carts",
    "apps.payments",
    "apps.notifications",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
SITE_ID = 1

AUTH_USER_MODEL = "users.User"
# CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"  # Specify the upload path
CKEDITOR_IMAGE_BACKEND = "pillow"  # Use the Pillow image processing library

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"


# Database

DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

DESCRIPTION = """Documentation of API endpoints of ecommerce application.

Handle Error Codes:
```json
    400: "Bad request.",
    401: "Unauthorized.",
    404: "Not found.",
    405: "Method not allowed.",
    500: "Internal server error.",
    200: "OK.",
    201: "Created.",
    202: "Accepted.",
```

Example:
```json
    {
        "status_code": 400,
        "exception_class": "ValidationError",
        "error_message": "Bad request."
    }
```
"""
SPECTACULAR_SETTINGS = {
    "TITLE": "E-commerce-Application API",
    "DESCRIPTION": DESCRIPTION,
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
}

DJOSER = {
    "ACTIVATION_URL": "api/v1/users/activate-account/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "api/v1/users/password-reset-account/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,
    "TOKEN_MODEL": False,
    "serializers": {
        "current_user": "apps.users.api.serializers.UserSerializer",
    },
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
}

API_PREFIX = "api/v1/"
PROTOCOL = "http"
DOMAIN = "localhost"
ACTIVATE_ACCOUNT_URL = "users/activation/"
RESET_PASS_CONFIRM_URL = "users/reset_password_confirm/"
