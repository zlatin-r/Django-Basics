from django.urls import path

from urls_and_views.core.views import index

urlpatterns = [
    path("<int:pk>/", index),
    path("<slug:slug>/", index),
    path("<int:pk>/<slug:slug>/", index),
]