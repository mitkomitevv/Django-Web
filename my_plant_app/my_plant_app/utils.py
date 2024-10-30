from my_plant_app.user_profile.models import Profile


def get_profile():
    return Profile.objects.last()