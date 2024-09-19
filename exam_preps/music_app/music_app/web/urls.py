from django.urls import path

from music_app.web.views import index, create_profile

urlpatterns = (
    path("", index, name="index"),
    path("create-profile/", create_profile,  name="create_profile"),
)