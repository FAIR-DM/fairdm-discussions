from django.urls import include, path

urlpatterns = [
    path("comments/", include("django_comments_xtd.urls")),
]
