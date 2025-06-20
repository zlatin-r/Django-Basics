from django.urls import path, include
from trips.views import *

urlpatterns = [
    path('create/', CreateTripView.as_view(), name='create-trip'),
    path('<int:pk>/', include([
        path('details/', DetailsTripView.as_view(), name='details-trip'),
        path('edit/', EditTripView.as_view(), name='edit-trip'),
        path('delete/', DeleteTripView.as_view(), name='delete-trip')
    ]))
]
