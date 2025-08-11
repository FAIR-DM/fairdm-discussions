# import flatattrs
from django import template
from django_comments_xtd import VERSION

register = template.Library()


@register.simple_tag
def javascript_version():
    return "django_comments_xtd/js/django-comments-xtd-{}.{}.{}.js".format(*VERSION)
