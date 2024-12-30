from django.urls import path

from common import views

urlpatterns = [
    path('', views.show_home_page, name="home"),
]