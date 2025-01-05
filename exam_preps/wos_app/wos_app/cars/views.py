from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from wos_app.cars.forms import CarCreateForm
from wos_app.cars.models import Car
from wos_app.common.utils import get_profile


class CarCreateView(CreateView):
    template_name = 'car/car-create.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)


class CarDetailsView(DetailView):
    model = Car
    template_name = 'car/car-details.html'

