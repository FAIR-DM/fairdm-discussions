# import flatattrs
from django import template
from django.templatetags.static import static
from django_comments_xtd import VERSION

register = template.Library()


@register.simple_tag
def comments_xtd_frontend():
    return static(
        "django_comments_xtd/js/django-comments-xtd-{}.{}.{}.js".format(*VERSION)
    )
