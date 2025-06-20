from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, TemplateView

from core.utils import get_traveler_obj, get_all_trips_obj
from traveler.forms import CreateProfileForm
from traveler.models import Traveler


class CreateTravelerView(CreateView):
    model = Traveler
    form_class = CreateProfileForm
    template_name = "traveler/create-traveler.html"
    success_url = reverse_lazy("all-trips")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler_obj()  # Add custom context
        return context


class DetailsTravelerView(TemplateView):
    template_name = "traveler/details-traveler.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["traveler"] = get_traveler_obj()
        context["all_trips"] = get_all_trips_obj()
        return context


class EditTravelerView(UpdateView):
    ...


class DeleteTravelerView(DeleteView):
    ...
