from django import template
from main.models import *
register = template.Library()

@register.simple_tag(name='getcoms')
def get_comments(filter=None):
    if not filter:
        return Comment.objects.all()
    else:
        return Comment.objects.filter(pk=filter)
@register.inclusion_tag('main/frr.html')
def show_comments(sort=None, com_selected=0):
    if not sort:
        coms=Comment.objects.all()
    else:
        coms=Comment.objects.order_by(sort)
    return {'coms':coms,'com_selected': com_selected}