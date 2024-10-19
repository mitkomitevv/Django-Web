from musicApp.profile_user.models import Profile


def get_profile():
    return Profile.objects.first()
