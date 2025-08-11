from django.utils.translation import gettext as _
from django_comments_xtd.api.serializers import ReadCommentSerializer
from rest_framework import serializers


class CustomReadCommentSerializer(ReadCommentSerializer):
    """Custom serializer that fetches information from the given user object rather than static info on the Comment model."""

    user_name = serializers.SerializerMethodField()
    user_url = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        """Return the user's name."""
        return str(obj.user) if obj.user else _("Anonymous")

    def get_user_url(self, obj):
        """Return the user's URL."""
        return obj.user.get_absolute_url() if obj.user else None
