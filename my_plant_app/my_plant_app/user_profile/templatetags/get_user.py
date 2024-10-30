from django import template
from my_plant_app.utils import get_profile

register = template.Library()

@register.simple_tag
def get_user():
    return get_profile()
