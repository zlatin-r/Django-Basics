from django.urls import path
from common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-trips/', views.all_trips_view, name='all-trips')
]
