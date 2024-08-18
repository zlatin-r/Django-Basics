from django.urls import path, include

from urls_and_views.core.views import index, index_json

urlpatterns = (
    path("<int:pk>/", index),
    path("<slug:slug>/", index),
    path("<int:pk>/<slug:slug>/", index),

    path('json/', include(
    [
        path('', index_json),
        path('<int:pk>/', index_json),
        path('<slug:slug>/', index_json),
        path('<int:pk>/<slug:slug>/', index_json)
    ])),
)

