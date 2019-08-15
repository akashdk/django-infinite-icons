import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-infinite-icons',
    version='0.1',
    packages=['infinite_icons', 'infinite_icons.templatetags'],
    include_package_data=True,
    url='https://github.com/akashdk/django-infinite-icons',
    description='Django-infinite-icons will help you to render SVG icons.',
    long_description=README,
    license='MIT License',  # example license
    requires=['django (>= 1.11)'],
    author='Akash Dhinagaran',
    author_email='imakkash@gmail.com',
    project_urls={
        'Documentation': 'https://github.com/akashdk/django-infinite-icons/blob/master/README.md',
        'Say Thanks!': 'https://akkash.me',
        'Source': 'https://github.com/akashdk/django-infinite-icons',
        'Tracker': 'https://github.com/akashdk/django-infinite-icons/issues',
    },    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'

    ],
)