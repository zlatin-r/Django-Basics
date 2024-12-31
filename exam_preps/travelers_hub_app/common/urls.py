from django.urls import path

from common import views
from common.views import AllTripsView

urlpatterns = [
    path('', views.show_home_page, name="home"),
    path('all-trips/', AllTripsView.as_view(), name='all-trips')
]
