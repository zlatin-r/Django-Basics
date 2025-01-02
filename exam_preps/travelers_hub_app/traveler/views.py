from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView

from traveler import models
from traveler.forms import TravelerCreateForm
from travelers_hub_app.utils import get_traveler_obj, get_all_trips


class TravelerCreateView(CreateView):
    model = models.Traveler
    form_class = TravelerCreateForm
    template_name = 'traveler/create-traveler.html'
    success_url = reverse_lazy('all-trips')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler_obj()  # Add custom context
        return context


class TravelerDetailsView(TemplateView):
    template_name = 'traveler/details-traveler.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['traveler'] = get_traveler_obj()
        context['trips'] = get_all_trips().order_by('-start_date')

        return context


class TravelerEditView(UpdateView):
    pass


class TravelerDeleteView(DeleteView):
    pass
