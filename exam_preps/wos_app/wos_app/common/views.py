from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from wos_app.cars.models import Car
from wos_app.common.utils import get_all_cars


class HomePage(TemplateView):
    template_name = 'index.html'


class CataloguePage(ListView):
    model = Car
    template_name = 'catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = get_all_cars()
        return context
