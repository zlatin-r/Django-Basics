from django.urls import path
from organizer.views import *

urlpatterns = [
    path('create/', CreateOrganizerView.as_view(), name='create-organizer'),
    path('details/', DetailsOrganizerView.as_view(), name='details-organizer'),
    path('edit/', EditOrganizerView.as_view(), name='edit-organizer'),
    path('delete/', DeleteOrganizerView.as_view(), name='delete-organizer'),
]
