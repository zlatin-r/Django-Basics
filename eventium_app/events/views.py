from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from common.utils import get_all_events, get_organizer_obj
from events.forms import EventCreateForm, EditEventForm, DeleteEventForm
from events.models import Events


class CreateEventView(CreateView):
    model = Events
    form_class = EventCreateForm
    template_name = "create-event.html"
    success_url = reverse_lazy("events")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = get_all_events()
        return context

    def form_valid(self, form):
        form.instance.organizer = get_organizer_obj()
        return super().form_valid(form)


class DetailsEventView(DetailView):
    model = Events
    template_name = "details-event.html"
    context_object_name = "event"
    pk_url_kwarg = 'event_pk'


class EditEventView(UpdateView):
    model = Events
    form_class = EditEventForm
    template_name = "edit-event.html"
    pk_url_kwarg = 'event_pk'

    def get_success_url(self):
        return reverse('details-event', kwargs={'event_pk': self.object.pk})


class DeleteEventView(DeleteView):
    model = Events
    template_name = "delete-event.html"
    form_class = DeleteEventForm
    success_url = reverse_lazy("events")
    pk_url_kwarg = "event_pk"

    def get_initial(self):
        return self.object.__dict__
