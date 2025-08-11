# myapp/signals.py
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django_comments_xtd.models import XtdComment
from fairdm.contrib.contributors.models import Person


@receiver(pre_save, sender=XtdComment)
def set_user_url_from_user(sender, instance, **kwargs):
    """
    Populate the `user_url` field for logged-in users
    using their get_absolute_url() method.
    """
    if instance.user_id and not instance.user_url:
        try:
            instance.user_url = instance.user.get_absolute_url()
        except AttributeError:
            # If get_absolute_url doesn't exist, skip
            pass


# @receiver(pre_save, sender=Person)
# def cache_changed_user_name(sender, instance, **kwargs):
#     """Cache the username for the Person instance before saving so we can use it later to
#     check if it has changed."""

#     instance.previous_user_name = instance.tracker.previous("name")


@receiver(pre_save, sender=Person)
def cache_changed_user_name(sender, instance, **kwargs):
    """
    Cache the previous name before saving so we can check in post_save if it changed.
    """
    # NOTE: We can't check this directly in the post_save signal because the instance
    # tracker will have already been reset during the save.
    if instance.pk:  # only for updates, not creation
        instance.previous_user_name = instance.tracker.previous("name")


@receiver(post_save, sender=Person)
def update_comment_user_name_if_username_changed(sender, instance, **kwargs):
    """
    If the user's display name changes, update all comments associated
    with that user to reflect the new name.
    """
    if hasattr(instance, "previous_user_name"):
        # Only update if actually changed
        if instance.name != instance.previous_user_name:
            XtdComment.objects.filter(user=instance).update(user_name=instance.name)
