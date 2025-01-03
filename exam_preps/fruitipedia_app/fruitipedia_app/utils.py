from fruitipedia_app.fruits.models import Fruit
from fruitipedia_app.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def get_all_fruits():
    return Fruit.objects.all()
