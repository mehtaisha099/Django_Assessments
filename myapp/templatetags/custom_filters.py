from django import template

register = template.Library()

@register.filter
def truncate_words(value, count):
    words = value.split()

    if len(words) <= count:
        return value

    return ' '.join(words[:count]) + '...'