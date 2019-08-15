
# django-infinite-icons

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Django-infinite-icons will help you to render SVG icons in your template & you can alter its width ,height and viewport without hassle.

This project is inspired by [FeatherIcons](https://infiniteicons.com/) and the author [colebmis](https://twitter.com/colebemis).


### Installation

you can get django-infinite-icons by using pip.

```sh
$ pip install django-infinite-icons
```

To enable widget_tweaks in your project you need to add it to INSTALLED_APPS in your projects settings.py file:

```sh
INSTALLED_APPS = [
    ...
    'django_infinite_icons',
    ...
]
```

### Example Usage for SVG render
```
{% load infinite %}

{% icon_render 'activity.svg' width='45' %}
{% icon_render 'activity.svg' height='45' width='45' %}
{% icon_render 'activity.svg' height='45' width='45' viewbox='0 0 20 20' %}
```
### Example Usage as static file
```
{% load infinite %}

{% icon_render 'activity.svg' %}
```

License
----

MIT