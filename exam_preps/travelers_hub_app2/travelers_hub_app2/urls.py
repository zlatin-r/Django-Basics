from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('trips/', include('trips.urls')),
    path('traveler/', include('traveler.urls')),
]
