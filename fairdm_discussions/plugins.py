from django.utils.translation import gettext_lazy as _
from django.views.generic.base import TemplateView
from fairdm import plugins
from fairdm.core.dataset.models import Dataset
from fairdm.core.measurement.models import Measurement
from fairdm.core.project.models import Project
from fairdm.core.sample.models import Sample


@plugins.register(Project, Dataset, Sample, Measurement)
class Discussion(plugins.Plugin, TemplateView):
    """
    Plugin for adding discussion/commenting functionality to FairDM objects.

    This plugin integrates django-comments-xtd to provide threaded discussions
    on Projects, Datasets, Samples, and Measurements.
    """

    menu = {
        "label": _("Discussion"),
        "icon": "comments",
    }
    template_name = "fairdm_discussions/discussion.html"
