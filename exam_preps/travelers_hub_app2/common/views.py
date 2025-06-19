from django.shortcuts import render

from core.utils import get_traveler_obj


def index(request):
    traveler = get_traveler_obj()
    context = {
        'traveler': traveler
    }
    return render(request, template_name='common/index.html', context=context)


def all_trips_view(request):
    pass
