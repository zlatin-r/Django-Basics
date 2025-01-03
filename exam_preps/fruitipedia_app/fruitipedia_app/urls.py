from django.contrib import admin
from django.urls import path, include

from fruitipedia_app.common import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
]
