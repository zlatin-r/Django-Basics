from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


class CreateAuthorView(CreateView):
    ...


class DetailsAuthorView(DetailView):
    ...


class EditAuthorView(UpdateView):
    ...


class DeleteAuthorView(DeleteView):
    ...
