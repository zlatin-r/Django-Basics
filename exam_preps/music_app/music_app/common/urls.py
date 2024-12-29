from django.urls import path

from music_app.common.views import HomePage

urlpatterns = (
    path("", HomePage.as_view(), name="home"),
)