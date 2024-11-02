from furry_funnies.author_profile.models import Author


def get_author():
    return Author.objects.last()