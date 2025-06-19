from django.shortcuts import render

from core.utils import get_profile


def index(request):
    traveler = get_profile()
    context = {
        'traveler': traveler
    }
    return render(request, template_name='common/index.html', context=context)


def all_trips_view(request):
    pass
