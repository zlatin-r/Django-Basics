from django import template

from travelers_hub_app.utils import get_traveler_obj

register = template.Library()


@register.simple_tag
def get_traveler():
    return get_traveler_obj()