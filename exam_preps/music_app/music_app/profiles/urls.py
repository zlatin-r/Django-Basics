from django.urls import path

from music_app.profiles.views import ProfileDetailView

urlpatterns = [
    path('details/', ProfileDetailView.as_view(), name='profile-details'),
]
