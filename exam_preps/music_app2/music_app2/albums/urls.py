from django.urls import path

from music_app.albums.views import CreateAlbumView

urlpatterns = (
    path("add/", CreateAlbumView.as_view(), name="create_album"),
)