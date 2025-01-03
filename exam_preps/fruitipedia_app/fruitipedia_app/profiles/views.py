from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia_app.profiles.forms import ProfileCreateForm


class ProfileCreateView(CreateView):
    template_name = 'profile/create-profile.html'
    form_class = ProfileCreateForm
    success_url = 'common/dashboard.html'


class ProfileDetailsView(DetailView):
    pass


class ProfileEditView(UpdateView):
    pass


class ProfileDeleteView(DeleteView):
    pass
