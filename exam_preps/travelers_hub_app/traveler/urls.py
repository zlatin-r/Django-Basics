from django.urls import path

from traveler import views
from traveler.views import TravelerCreateView, TravelerDetailsView, TravelerEditView, TravelerDeleteView

urlpatterns = [
    path('create/', TravelerCreateView.as_view(), name='add-traveler'),
    path('details/', TravelerDetailsView.as_view(), name='traveler-details'),
    path('edit/', TravelerEditView.as_view(), name='traveler-edit'),
    path('delete/', TravelerDeleteView.as_view(), name='traveler-delete')
]
