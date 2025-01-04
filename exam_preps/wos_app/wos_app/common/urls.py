from django.urls import path

from wos_app.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('catalogue/', views.CataloguePage.as_view(), name='catalogue')
]