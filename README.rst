==========
django-tla
==========

This is a simple pluggable application that allows your Django-powered site to host ads from the `Text Link Ads`_ service. Unfortunately, repeated attempts to try and get the staff at TLA to create code for Django have fallen on deaf ears, so this is technically a port of their Ruby on Rails configuration.

There are no database models and some configuration is required.

.. _Text Link Ads: http://text-link-ads.com/

Installing django-tla
---------------------

1. Download the tarball, extract it and add ``tla`` to your ``PYTHONPATH``.
2. Add ``tla`` to your to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        # ...
        'tla',
    )
    
3. Add ``TLA_INVENTORY_KEY`` to your settings file. You can get your inventory key (or XML key) by logging into Text Link Ads and `visiting this page`_.
4. Add ``{% load tla %}`` to the top of the template you want to display links on.
5. Add ``{% tla_list %}`` to where you wish to display the list of links.
6. (optional) Unlike the automagically generated code that Text Link Ads gives you, there are no inline styles. The list has an ID of ``tla``, so it can be targeted in your stylesheets.

.. _visiting this page: http://www.text-link-ads.com/my_account.php?view=my_sites

And then that should be it! Hopefully. :)