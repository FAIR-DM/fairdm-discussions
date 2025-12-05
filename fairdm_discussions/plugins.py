import waffle
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import TemplateView
from fairdm import plugins
from fairdm.core.dataset.models import Dataset
from fairdm.core.measurement.models import Measurement
from fairdm.core.project.models import Project
from fairdm.core.sample.models import Sample


@plugins.register(Project, Dataset, Sample, Measurement)
class Discussion(plugins.FairDMPlugin, TemplateView):
    """
    Plugin for adding discussion/commenting functionality to FairDM objects.

    This plugin integrates django-comments-xtd to provide threaded discussions
    on Projects, Datasets, Samples, and Measurements. It requires the waffle
    switch 'allow_discussions' to be enabled.
    """

    title = _("Discussion")
    menu_item = plugins.PluginMenuItem(
        name=_("Discussion"),
        category=plugins.EXPLORE,
        icon="comments",
    )
    template_name = "fairdm_discussions/discussion.html"

    def dispatch(self, request, *args, **kwargs):
        """
        Override dispatch to check if the discussion plugin is enabled via waffle switch.
        """
        if not waffle.switch_is_active("allow_discussions"):
            raise PermissionDenied(
                _("Discussions have not been enabled for this site.")
            )
        return super().dispatch(request, *args, **kwargs)
