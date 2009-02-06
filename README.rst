==========
django-tla
==========

This is a simple pluggable application that allows your Django-powered site to host ads from the Text-Link-Ads_ service. Unfortunately, repeated attempts to try and get the staff at TLA to create code for Django have fallen on deaf ears, so this is technically a port of their Ruby on Rails configuration.

There are no database models and no configuration is required.

.. _Text-Link-Ads: http://text-link-ads.com/

Installing django-tla
---------------------

1. Download the tarball, extract it and add ``tla`` to your ``PYTHONPATH``.
2. Add ``tla`` to your to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        # ...
        'tla',
    )
    
And that's it! Hopefully. :)
