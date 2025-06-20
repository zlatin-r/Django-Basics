from traveler.models import Traveler
from trips.models import Trip


def get_traveler_obj():
    return Traveler.objects.first()


def get_all_trips_obj():
    return Trip.objects.all()