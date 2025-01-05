from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from wos_app.cars.models import Car
from wos_app.common.utils import get_profile
from wos_app.user_profile.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm


class ProfileCreateView(CreateView):
    template_name = 'profile/profile-create.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')


class ProfileDetailsView(DetailView):
    context_object_name = 'user'
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()

        total_price = Car.objects.aggregate(Sum('price'))['price__sum'] or 0

        context['user'] = profile
        context['total_price'] = total_price
        context['full_name'] = f"{profile.first_name} {profile.last_name}"

        return context


class ProfileEditView(UpdateView):
    template_name = 'profile/profile-edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    form_class = ProfileDeleteForm
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_profile()
