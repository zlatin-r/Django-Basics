from events.models import Events
from organizer.models import Organizer


def get_organizer_obj():
    return Organizer.objects.first()


def get_all_events():
    return Events.objects.all()
