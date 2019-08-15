import re
from django import template
# from django.contrib.staticfiles.templatetags.staticfiles import static
from django.templatetags.static import static
from django.conf import setting

register = template.Library()


@register.simple_tag
def icon(path, width=None, height=None, viewport=None):
    print(path, width, height, viewport)
    p = re.compile(r'width=')
    print(open(static("feather/award.svg"), 'r'))
    return static("feather/award.svg")

@register.simple_tag
def icon_render(path, width=None, height=None, viewport=None):
    print(path, width, height, viewport)
    p = re.compile(r'width=')
    print(open(static("feather/award.svg"), 'r'))
    return static("feather/award.svg")
