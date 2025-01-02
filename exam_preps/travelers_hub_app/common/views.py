from django.shortcuts import render
from django.views.generic import ListView

from travelers_hub_app.utils import get_all_trips, get_traveler_obj
from trip.models import Trip


def show_home_page(request):
    return render(request, template_name='common/index.html')


class AllTripsView(ListView):
    model = Trip
    context_object_name = 'all_trips'
    template_name = 'common/all-trips.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_traveler_obj()  # Add custom context for the traveler
        return context
