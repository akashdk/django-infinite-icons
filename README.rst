django-infinite-icons
=====================

|Build Status|

Django-infinite-icons will help you to render SVG icons in your template
& you can alter its width ,height and viewport without hassle.

This project is inspired by
`FeatherIcons <https://feathericons.com/>`__ and the author
`colebmis <https://twitter.com/colebemis>`__.

Installation
~~~~~~~~~~~~

you can get django-infinite-icons by using pip.

.. code:: sh

    $ pip install django-infinite-icons

To enable widget\_tweaks in your project you need to add it to
INSTALLED\_APPS in your projects settings.py file:

.. code:: sh

    INSTALLED_APPS = [
        ...
        'infinite_icons',
        ...
    ]

Example Usage for SVG render
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    {% load infinite %}

    {% icon_render 'activity.svg' width='45' %}
    {% icon_render 'activity.svg' height='45' width='45' %}
    {% icon_render 'activity.svg' height='45' width='45' viewbox='0 0 20 20' %}

Example Usage load as static file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    {% load infinite %}

    {% icon 'activity.svg' %}


License
-------

`MIT <https://github.com/akashdk/django-infinite-icons/blob/master/LICENSE>`__

.. |Build Status| image:: https://travis-ci.org/joemccann/dillinger.svg?branch=master
   :target: https://travis-ci.org/joemccann/dillinger
