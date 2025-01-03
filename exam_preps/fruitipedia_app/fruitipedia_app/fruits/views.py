from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia_app.fruits.forms import FruitCreateForm, FruitEditForm
from fruitipedia_app.fruits.models import Fruit
from fruitipedia_app.utils import get_profile


class FruitCreateView(CreateView):
    form_class = FruitCreateForm
    template_name = 'fruit/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)



class FruitDetailsView(DetailView):
    model = Fruit
    template_name = 'fruit/details-fruit.html'
    context_object_name = 'fruit'


class FruitEditView(UpdateView):
    model = Fruit
    form_class = FruitEditForm
    template_name = 'fruit/edit-fruit.html'
    success_url = reverse_lazy('dashboard')


class FruitDeleteView(DeleteView):
    pass
