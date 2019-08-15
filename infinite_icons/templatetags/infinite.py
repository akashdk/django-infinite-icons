from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from infinite_icons.svg_data import data

register = template.Library()


@register.simple_tag
def icon(file_name=None):
    file_ = "feather/" + file_name
    return static(file_)


@register.simple_tag
def icon_render(file_name=None, **kwargs):
    width = kwargs.get("width", "")
    height = kwargs.get("height", "")
    viewbox = kwargs.get("viewbox", "")
    svg = data.get(file_name, "")
    if width:
        width = "width='%s'" % width
        svg = svg.replace("width='24'", width)
    if height:
        height = "height='%s'" % height
        svg = svg.replace("height='24'", height)
    if viewbox:
        viewbox = "'viewBox=%s'" % viewbox
        svg = svg.replace("viewBox='0 0 24 24'", viewbox)
    return mark_safe(svg)
