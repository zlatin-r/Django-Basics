from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


class TripCreateView(CreateView):
    pass


class TripDetailsView(DetailView):
    pass


class TripEditView(UpdateView):
    pass


class TripDeleteView(DeleteView):
    pass
