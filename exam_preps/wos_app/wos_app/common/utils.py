from wos_app.user_profile.models import UserProfile

def get_profile():
    return UserProfile.objects.first()