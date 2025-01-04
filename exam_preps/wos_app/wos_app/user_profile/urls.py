from django.urls import path

from wos_app.user_profile import views

urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='create-profile'),
]


# 	http://localhost:8000/profile/create - Profile create page
# 	http://localhost:8000/profile/details/ - Profile details page
# 	http://localhost:8000/profile/edit/ - Profile edit page
# 	http://localhost:8000/profile/delete/ - Profile delete page
