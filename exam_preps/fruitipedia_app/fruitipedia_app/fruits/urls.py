from django.urls import path, include

from fruitipedia_app.fruits import views

urlpatterns = [
    path('create/', views.FruitCreateView.as_view(), name='fruit-create'),
    path('<int:fruit_id>/', include([
        path('details/', views.FruitDetailsView, name='fruit-details'),
        path('edit/', views.FruitEditView, name='fruit-edit'),
        path('delete/', views.FruitDeleteView, name='fruit-delete'),]
    ))
]
