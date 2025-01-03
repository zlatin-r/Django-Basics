from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia_app.profiles.forms import ProfileCreateForm
from fruitipedia_app.profiles.models import Profile
from fruitipedia_app.utils import get_profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class ProfileDetailsView(DetailView):
    pass


class ProfileEditView(UpdateView):
    pass


class ProfileDeleteView(DeleteView):
    pass
