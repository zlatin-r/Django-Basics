from django.urls import path
from common import views

urlpatterns = [
    path('', views.index, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
