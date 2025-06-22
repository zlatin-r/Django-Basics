from django.urls import path
from common import views

urlpatterns = [
    path('', views.index_view, name="home"),
    path('events/', views.all_events_view, name="events"),
]
