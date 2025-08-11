import waffle
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import TemplateView
from fairdm import plugins


class DiscussionPlugin(plugins.Explore, TemplateView):
    name = "discussion"
    title = _("Discussion")
    menu_item = {
        "name": _("Discussion"),
        "icon": "comments",
    }
    icon = "comments"
    template_name = "fairdm_discussions/discussion.html"

    sidebar_secondary_config = {
        "visible": True
    }  # Hide the secondary sidebar by default

    def dispatch(self, request, *args, **kwargs):
        """
        Override dispatch to check if the discussion plugin is enabled.
        """
        if not self.check(request, self.base_object, **kwargs):
            raise Http404(_("This plugin has not been enabled."))
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def check(request, instance, **kwargs):
        """
        Check if the user has permission to view the discussion plugin.
        This can be overridden in subclasses to implement custom logic.
        """
        return waffle.switch_is_active("allow_discussions")


plugins.dataset.register(DiscussionPlugin)
plugins.project.register(DiscussionPlugin)
plugins.sample.register(DiscussionPlugin)
plugins.measurement.register(DiscussionPlugin)
