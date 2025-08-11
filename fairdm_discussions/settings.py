"""
Default settings for the commenting system built in to FairDM.
"""

EASY_ICONS = globals().get("EASY_ICONS", {})
INSTALLED_APPS = globals().get("INSTALLED_APPS", [])
SITE_DOMAIN = globals().get("SITE_DOMAIN")

COMMENTS_APP = "django_comments_xtd"
COMMENTS_XTD_THREADED_EMAILS = True
COMMENTS_XTD_API_GET_USER_AVATAR = "fairdm.contrib.contributors.utils.get_avatar_url"
COMMENTS_XTD_API_USER_REPR = lambda u: str(u)

COMMENTS_XTD_MAX_THREAD_LEVEL = 8  # Maximum depth for comment threads
COMMENTS_XTD_LIST_ORDER = ("-thread_id", "order")  # Default comment ordering
COMMENTS_XTD_APP_MODEL_OPTIONS = {
    "default": {
        "allow_flagging": True,
        "allow_feedback": True,
        "show_feedback": True,
        "who_can_post": "users",  # NOTE: this app is not tested for anonymous comments. Changes to this value may have unintended consequences.
    }
}

COMMENTS_XTD_FROM_EMAIL = f"noreply@{SITE_DOMAIN}"
COMMENTS_XTD_CONTACT_EMAIL = f"noreply@{SITE_DOMAIN}"

# Add the comments icon to the EASY_ICONS dictionary
EASY_ICONS.get("aliases", {}).update(
    {
        "comments": "fas fa-comments",  # Ensure the comments icon is set correctly
    }
)

# Ensure the FairDM discussions app and dependencies are included in the installed apps
INSTALLED_APPS += [
    "fairdm_discussions",
    "django_comments_xtd",
    "django_comments",
]
