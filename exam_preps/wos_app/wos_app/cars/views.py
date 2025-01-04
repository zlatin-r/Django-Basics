from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from wos_app.cars.forms import CarCreateForm


class CarCreateView(CreateView):
    template_name = 'car/car-create.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('catalogue')
