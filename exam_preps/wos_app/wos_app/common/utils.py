from wos_app.cars.models import Car
from wos_app.user_profile.models import UserProfile

def get_profile():
    return UserProfile.objects.first()

def get_all_cars():
    return Car.objects.all()