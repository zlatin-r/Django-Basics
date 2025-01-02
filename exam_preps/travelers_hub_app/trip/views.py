from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from trip.models import Trip


class TripCreateView(CreateView):
    model = Trip
    template_name = 'trip/create-trip.html'


class TripDetailsView(DetailView):
    pass


class TripEditView(UpdateView):
    pass


class TripDeleteView(DeleteView):
    pass
