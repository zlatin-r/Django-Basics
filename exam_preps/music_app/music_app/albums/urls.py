from music_app.albums import views
from django.urls import path

urlpatterns = [
    path('add/', views.AlbumCreateView.as_view(), name='add-album'),
]