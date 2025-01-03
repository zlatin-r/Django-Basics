from django.views.generic import TemplateView

from fruitipedia_app.fruits.models import Fruit
from fruitipedia_app.utils import get_all_fruits


class HomePage(TemplateView):
    template_name = 'index.html'


class Dashboard(TemplateView):
    model = Fruit
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruits'] = get_all_fruits()
        return context
