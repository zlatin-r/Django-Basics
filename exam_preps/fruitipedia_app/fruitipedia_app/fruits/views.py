from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia_app.fruits.forms import FruitCreateForm
from fruitipedia_app.utils import get_profile


class FruitCreateView(CreateView):
    form_class = FruitCreateForm
    template_name = 'fruit/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)



class FruitDetailsView(DetailView):
    pass


class FruitEditView(UpdateView):
    pass


class FruitDeleteView(DeleteView):
    pass
