"""
Test-specific Django settings for fairdm-discussions test suite.

Imports base FairDM configuration then overrides for fast, isolated testing.
"""

import logging
import sys
import tempfile
from pathlib import Path

# Silence noisy loggers during tests
logging.disable(logging.CRITICAL)

import fairdm

fairdm.setup(
    apps=["fairdm_demo"],
    addons=["fairdm_discussions"],
)

ROOT_URLCONF = "fairdm.conf.urls"

# ==============================================================================
# TEST DATABASE
# ==============================================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "ATOMIC_REQUESTS": True,
        "TEST": {
            "NAME": ":memory:",
        },
    }
}

# ==============================================================================
# MIGRATIONS
# ==============================================================================


class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

    def setdefault(self, key, default=None):
        return None


MIGRATION_MODULES = DisableMigrations()

# ==============================================================================
# SECURITY — disable redirects and strict settings for tests
# ==============================================================================
DEBUG = True
SECRET_KEY = "test-secret-key-not-for-production-use-only"
ALLOWED_HOSTS = ["*"]
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = None
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# ==============================================================================
# PASSWORD HASHING
# ==============================================================================
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# ==============================================================================
# CACHING
# ==============================================================================
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
    "select2": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
}

# ==============================================================================
# EMAIL
# ==============================================================================
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# ==============================================================================
# STATIC FILES & MEDIA
# ==============================================================================
COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False
MEDIA_ROOT = Path(tempfile.gettempdir()) / "fairdm_discussions_test_media"
STATIC_ROOT = Path(tempfile.gettempdir()) / "fairdm_discussions_test_static"

# ==============================================================================
# CELERY
# ==============================================================================
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# ==============================================================================
# LOGGING
# ==============================================================================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stderr,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "ERROR",
    },
}

# ==============================================================================
# TEMPLATES — remove context processors that don't exist in test environment
# ==============================================================================
for _template_config in TEMPLATES:  # noqa: F405
    if "OPTIONS" in _template_config and "context_processors" in _template_config["OPTIONS"]:
        _template_config["OPTIONS"]["context_processors"] = [
            cp for cp in _template_config["OPTIONS"]["context_processors"] if "mvp.context_processors" not in cp
        ]
