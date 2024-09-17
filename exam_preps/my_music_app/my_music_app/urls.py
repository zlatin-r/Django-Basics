from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("my_music_app.home.urls")),
    path("albums/", include("my_music_app.albums.urls")),
    path("profiles/", include("my_music_app.profiles.urls")),
]
