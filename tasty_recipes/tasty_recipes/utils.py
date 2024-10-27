from tasty_recipes.user_profile.models import Profile


def get_profile():
    return Profile.objects.last()