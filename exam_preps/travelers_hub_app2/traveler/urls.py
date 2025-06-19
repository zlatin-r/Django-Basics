from django.urls import path
from traveler.views import *

urlpatterns = [
    path('create/', CreateTravelerView.as_view(), name='create-traveler'),
    path('details/', DetailsTravelerView.as_view(), name='details-traveler'),
    path('edit/', EditTravelerView.as_view(), name='edit-traveler'),
    path('delete/', DeleteTravelerView.as_view(), name='delete-traveler'),
]
