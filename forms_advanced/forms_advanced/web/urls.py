from django.urls import path

from forms_advanced.web.views import index, create_person

urlpatterns = (
    path("", index, name="index"),
    path("create/person/", create_person, name="create_person"),
)