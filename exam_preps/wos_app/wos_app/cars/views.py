from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from wos_app.cars.forms import CarCreateForm, CarDeleteForm
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


class CarEditView(UpdateView):
    model = Car
    fields = ('type', 'model', 'year', 'image_url', 'price')
    template_name = 'car/car-edit.html'
    success_url = reverse_lazy('catalogue')


class CarDeleteView(DeleteView):
    model = Car
    form_class = CarDeleteForm
    template_name = 'car/car-delete.html'
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)