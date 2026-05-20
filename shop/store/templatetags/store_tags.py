from django import template
from store.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.filter(parent =True)

@register.simple_tag()
def get_categories_l():
    return Category.objects.filter(parent=None)

@register.simple_tag()
def get_subcategories(category):
    return Category.objects.filter(parent=category)

@register.simple_tag()
def get_sorted():
    sorters =[
        {
            'title': 'Price',
            'sorters': [
                ('-price','Expensive'),
                ('price','Cheap'),

            ]
        },
        {
            'title': 'Color',
            'sorters': [
                ('color', 'A-Z'),
                ('-color', 'Z-A'),

            ]
        },
        {
            'title': 'Size',
            'sorters': [
                ('size', 'Small'),
                ('-size', 'Normal'),

            ]
        }
    ]
    return sorters