from django.apps import AppConfig


class FairDMDiscussionsConfig(AppConfig):
    name = "fairdm_discussions"

    def ready(self):
        from django_comments_xtd.api import CommentList

        from fairdm_discussions.serializers import CustomReadCommentSerializer

        CommentList.serializer_class = CustomReadCommentSerializer
