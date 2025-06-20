from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


class CreatePostView(CreateView):
    ...


class DetailsPostView(DetailView):
    ...


class EditPostView(UpdateView):
    ...


class DeletePostView(DeleteView):
    ...
