
# django-feather-icons

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Django-feather-icons will help you to render SVG icons in your template & you can alter its width ,height and viewport without hassle.

This project is inspired by [FeatherIcons](https://feathericons.com/) and the author [colebmis](https://twitter.com/colebemis).


### Installation

you can get django-feather-icons by using pip.

```sh
$ pip install django-feather-icons
```

To enable widget_tweaks in your project you need to add it to INSTALLED_APPS in your projects settings.py file:

```sh
INSTALLED_APPS = [
    ...
    'django_feather_icons',
    ...
]
```

### Example Usage
```
{% load django_feather_icons %}

{% love.svg witdh=50 height=50 %}
```

License
----

MIT