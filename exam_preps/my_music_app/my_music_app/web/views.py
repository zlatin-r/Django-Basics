from django.shortcuts import render

from my_music_app.common.profile_helpers import get_profile

def create_profile(request):
    return render(request, "home/home-no-profile.html")

def index(request):
    profile = get_profile()

    if profile is not None:
        return create_profile(request)

    return render(request, "home/home-with-profile.html")
