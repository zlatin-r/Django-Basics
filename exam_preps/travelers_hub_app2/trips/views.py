from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView


class CreateTripView(CreateView):
    ...


class DetailsTripView(DetailView):
    ...


class EditTripView(UpdateView):
    ...


class DeleteTripView(DeleteView):
    ...
