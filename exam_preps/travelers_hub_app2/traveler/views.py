from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from core.utils import get_traveler_obj
from traveler.forms import CreateProfileForm
from traveler.models import Traveler


class CreateTravelerView(CreateView):
    model = Traveler
    form_class = CreateProfileForm
    template_name = "traveler/create-traveler.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler_obj()  # Add custom context
        return context


class DetailsTravelerView(DetailView):
    ...


class EditTravelerView(UpdateView):
    ...


class DeleteTravelerView(DeleteView):
    ...
