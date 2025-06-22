from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from common.utils import get_organizer_obj, get_all_events
from organizer.forms import ProfileCreateForm, EditProfileForm
from organizer.models import Organizer


class CreateOrganizerView(CreateView):
    model = Organizer
    form_class = ProfileCreateForm
    template_name = "create-organizer.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = get_organizer_obj()
        return context


class DetailsOrganizerView(DetailView):
    template_name = "details-organizer.html"

    def get_object(self, queryset=None):
        return get_organizer_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["organizer"] = get_organizer_obj()
        context["events"] = get_all_events()
        return context


class EditOrganizerView(UpdateView):
    model = Organizer
    template_name = "edit-organizer.html"
    form_class = EditProfileForm
    success_url = reverse_lazy("details-organizer")

    def get_object(self, queryset=None):
        return get_organizer_obj()


class DeleteOrganizerView(DeleteView):
    model = Organizer
    template_name = "delete-organizer.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return get_organizer_obj()

    def post(self, request, *args, **kwargs):
        organizer = self.get_object()
        now = timezone.now()

        upcoming_events = organizer.events_set.filter(start_time__gt=now).exists()

        if not upcoming_events:
            organizer.delete()

        return redirect("home")
