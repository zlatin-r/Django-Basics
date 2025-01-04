from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia_app.fruits.models import Fruit
from fruitipedia_app.profiles.forms import ProfileCreateForm, ProfileEditForm
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
    model = Profile
    template_name = 'profile/details-profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = self.object
        posts_count = Fruit.objects.filter(owner=profile).count()
        context['posts_count'] = posts_count

        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/edit-profile.html'


class ProfileDeleteView(DeleteView):
    pass
