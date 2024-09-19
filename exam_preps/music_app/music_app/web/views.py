from django.shortcuts import render

from music_app.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def create_profile(request):
    return render(request, "web/home-no-profile.html")


def index(request):
    profile = get_profile()

    if profile is None:
        create_profile(request)

    return render(request, "web/home-with-profile.html")
