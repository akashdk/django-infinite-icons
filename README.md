
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

### Example Usage
```
{% load infinite %}

{% love.svg width=50 height=50 %}
```

License
----

MIT