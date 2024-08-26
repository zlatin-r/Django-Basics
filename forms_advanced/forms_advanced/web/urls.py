from django.urls import path

from forms_advanced.web.views import index

urlpatterns = (
    path("", index, name="index"),
)