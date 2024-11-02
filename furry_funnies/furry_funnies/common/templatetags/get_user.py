from django import template
from furry_funnies.utils import get_author


register = template.Library()


@register.simple_tag
def get_user():
    return get_author()
