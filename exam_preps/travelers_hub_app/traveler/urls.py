from django.urls import path

from traveler import views

urlpatterns = [
    path('create/', views.TravelerCreateView.as_view(), name='add-traveler'),
    path('details/', views.TravelerDetailsView.as_view(), name='traveler-details'),
    path('edit/', views.TravelerEditView.as_view(), name='traveler-edit'),
    path('delete/', views.TravelerDeleteView.as_view(), name='traveler-delete')
]
