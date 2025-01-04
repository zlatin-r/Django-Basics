from django.urls import reverse_lazy
from django.views.generic import CreateView

from wos_app.user_profile.forms import ProfileCreateForm


class ProfileCreateView(CreateView):
    template_name = 'profile/profile-create.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

