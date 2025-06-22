from django.urls import path, include
from events.views import *

urlpatterns = [
    path('create/', CreateEventView.as_view(), name='create-event'),
    path('<int:event_pk>/', include([
        path('details/', DetailsEventView.as_view(), name='details-event'),
        path('edit/', EditEventView.as_view(), name='edit-event'),
        path('delete/', DeleteEventView.as_view(), name='delete-event'),
    ]))
]
