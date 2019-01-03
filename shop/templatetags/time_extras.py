from datetime import datetime, timedelta

from django import template
from django.utils.timesince import timesince

register = template.Library()


@register.filter
def age_of_product(product):
    now = datetime.now()
    try:
        difference = now - product
    except:
        return product

    if difference <= timedelta(minutes=1):
        return 'just now'
    return '%(time)s ago' % {'time': timesince(product).split(', '[0])}
