from django.urls import path

from wos_app.cars import views

urlpatterns = [
    path('create/', views.CarCreateView.as_view(), name='create-car'),
]


# 	http://localhost:8000/car/catalogue/ - Catalogue page
# 	http://localhost:8000/car/create/ - Car create page
# 	http://localhost:8000/car/<id>/details/ - Car details page
# 	http://localhost:8000/car/<id>/edit/ - Car edit page
# 	http://localhost:8000/car/<id>/delete/ - Car delete page
