from django.urls import path, include

from urls_and_views.departments.views import department_details, department_details_by_name

urlpatterns = (
    # path("departments/1/", department_1_details),
    # path("departments/2/", department_2_details),
    path("", include("urls_and_views.core.urls")),
    path("<int:pk>/", department_details),
    path("<str:name>/", department_details_by_name),
)