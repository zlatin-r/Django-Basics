from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from core.utils import get_traveler_obj
from trips.forms import CreateTripForm, EditTripForm, DeleteTripForm
from trips.models import Trip


class CreateTripView(CreateView):
    model = Trip
    form_class = CreateTripForm
    template_name = "trips/create-trip.html"
    success_url = reverse_lazy("all-trips")

    def form_valid(self, form):
        form.instance.traveler = get_traveler_obj()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["traveler"] = get_traveler_obj()
        return context


class DetailsTripView(DetailView):
    model = Trip
    template_name = "trips/details-trip.html"
    context_object_name = "trip"



class EditTripView(UpdateView):
    model = Trip
    form_class = EditTripForm
    template_name = "trips/edit-trip.html"
    success_url = reverse_lazy("all-trips")



class DeleteTripView(DeleteView):
    model = Trip
    form_class = DeleteTripForm
    template_name = "trips/delete-trip.html"
    success_url = reverse_lazy("all-trips")

    def get_initial(self):
        return self.object.__dict__
