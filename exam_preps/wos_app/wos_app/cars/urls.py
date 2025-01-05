from django.urls import path, include

from wos_app.cars import views

urlpatterns = [
    path('create/', views.CarCreateView.as_view(), name='create-car'),
    path('<int:pk>/', include([
        path('details/', views.CarDetailsView.as_view(), name='details-car'),
        path('edti/', views.CarEditView.as_view(), name='edit-car'),
        path('delete/', views.CarDeleteView.as_view(), name='delete-car')
    ]))
]

# 	http://localhost:8000/car/create/ - Car create page
# 	http://localhost:8000/car/<id>/details/ - Car details page
# 	http://localhost:8000/car/<id>/edit/ - Car edit page
# 	http://localhost:8000/car/<id>/delete/ - Car delete page
