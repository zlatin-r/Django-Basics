from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from music_app.albums.models import Album
from music_app.profiles.forms import ProfileCreateForm
from music_app.utils import get_user_obj


class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_user_obj

        if profile:
            return ['profiles/home-with-profile.html']

        return ['profiles/home-no-profile.html']
