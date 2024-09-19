from django.shortcuts import render, redirect

from common.profile_helpers import get_profile
from music_app.albums.models import Album
from music_app.web.forms import CreateProfileForm


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    context = {
        "form": form
    }
    return render(request, "web/home-no-profile.html", context)


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    context = {
        "albums": Album.objects.all(),
    }

    return render(request, "web/home-with-profile.html", context)

# CBV:

# class IndexView(views.TemplateView):
#     def get_template_names(self):
#         if get_profile() is None:
#             return ["web/home-no-profile.html"]
#         return ["web/home-with-profile.html"]
