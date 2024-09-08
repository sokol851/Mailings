from django import template

register = template.Library()


# Создание тега
@register.simple_tag
def refactor(image):
    if image:
        return f'/media/{image}'
    return '#'
