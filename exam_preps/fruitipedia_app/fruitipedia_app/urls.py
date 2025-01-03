from django.contrib import admin
from django.urls import path, include

from fruitipedia_app.common import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fruitipedia_app.common.urls')),
    path('profile/', include('fruitipedia_app.profiles.urls')),
    path('fruit/', include('fruitipedia_app.fruits.urls')),
]
