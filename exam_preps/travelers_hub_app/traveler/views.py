from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView

from traveler import models
from traveler.forms import TravelerCreateForm, TravelerEditForm
from traveler.models import Traveler
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
    model = Traveler
    form_class = TravelerEditForm
    template_name = 'traveler/edit-traveler.html'
    success_url = reverse_lazy('traveler-details')

    def get_object(self, queryset=None):
        return get_traveler_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler_obj()
        return context

    def get_initial(self):
        return self.object.__dict__


class TravelerDeleteView(DeleteView):
    model = Traveler
    template_name = 'traveler/delete-traveler.html'
    context_object_name = 'traveler'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_traveler_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler_obj()  # Add traveler to the context
        return context