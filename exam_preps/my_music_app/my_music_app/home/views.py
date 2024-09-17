from django.shortcuts import render


def index(request):
    return render(request, "home/home-no-profile.html")
