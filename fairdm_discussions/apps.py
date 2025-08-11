from django.apps import AppConfig


class FairDMDiscussionsConfig(AppConfig):
    name = "fairdm_discussions"

    def ready(self):
        from . import signals  # noqa
