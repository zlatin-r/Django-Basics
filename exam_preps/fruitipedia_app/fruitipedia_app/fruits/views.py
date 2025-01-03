from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


class FruitCreateView(CreateView):
    pass


class FruitDetailsView(DetailView):
    pass


class FruitEditView(UpdateView):
    pass


class FruitDeleteView(DeleteView):
    pass
