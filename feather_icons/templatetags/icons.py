import re
from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static

register = template.Library()


@register.filter
def lower(path, width, height, viewport):
    print(path, width, height, viewport)
    p = re.compile(r'width=')
    return static("path.svg")
