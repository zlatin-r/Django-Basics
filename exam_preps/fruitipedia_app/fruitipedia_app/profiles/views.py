from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


class ProfileCreateView(CreateView):
    pass


class ProfileDetailsView(DetailView):
    pass


class ProfileEditView(UpdateView):
    pass


class ProfileDeleteView(DeleteView):
    pass
