from django.urls import path, include

from trip import views

urlpatterns = [
    path('crete/', views.TripCreateView.as_view(), name='add-trip'),
    path('<int:pk>', include([
        path('details/', views.TripDetailsView.as_view(), name='trip-details'),
        path('edit/', views.TripEditView.as_view(), name='trip-edit'),
        path('delete/', views.TripDeleteView.as_view(), name='delete-trip')
    ]))
]
