from world_of_speed.user_profile.models import Profile


def get_profile():
    return Profile.objects.last()
