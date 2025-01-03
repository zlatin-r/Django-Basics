from django.urls import path

from fruitipedia_app.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]