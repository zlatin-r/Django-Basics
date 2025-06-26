from django.shortcuts import render

from common.utils import get_organizer_obj, get_all_events


def index_view(request):
    organizer = get_organizer_obj()
    context = {
        "organizer": organizer
    }
    return render(request, template_name="index.html", context=context)


def all_events_view(request):
    organizer = get_organizer_obj()
    events = get_all_events()
    context = {
        "organizer": organizer,
        "events": events
    }
    return render(request, template_name="events.html", context=context)


