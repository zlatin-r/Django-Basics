from music_app2.profiles import Profile


def get_user_obj():
    return Profile.objects.first()
