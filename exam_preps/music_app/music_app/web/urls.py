from django.urls import path

from music_app.web.views import index

urlpatterns = (
    path("", index, name="index"),
)