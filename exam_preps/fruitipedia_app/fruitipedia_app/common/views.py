from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'common/index.html'


class Dashboard(TemplateView):
    template_name = 'common/dashboard.html'
