from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from travelers_hub_app.utils import get_traveler_obj
from trip.forms import CreateTripForm, EditTripForm, DeleteTripForm
from trip.models import Trip


class TripCreateView(CreateView):
    model = Trip
    form_class = CreateTripForm
    template_name = 'trip/create-trip.html'
    success_url = reverse_lazy('all-trips')

    def form_valid(self, form):
        form.instance.traveler = get_traveler_obj()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler_obj()
        return context


class TripDetailsView(DetailView):
    model = Trip
    template_name = 'trip/details-trip.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler_obj()
        return context


class TripEditView(UpdateView):
    model = Trip
    form_class = EditTripForm
    template_name = 'trip/edit-trip.html'
    success_url = reverse_lazy('all-trips')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler_obj()  # Add traveler to context
        return context


class TripDeleteView(DeleteView):
    model = Trip
    template_name = 'trip/delete-trip.html'
    form_class = DeleteTripForm
    success_url = reverse_lazy('all-trips')

    def get_initial(self):
        return self.object.__dict__
