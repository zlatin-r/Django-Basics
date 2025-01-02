from traveler.models import Traveler
from trip.models import Trip


def get_traveler_obj():
    return Traveler.objects.first()


def get_all_trips():
    return Trip.objects.all()