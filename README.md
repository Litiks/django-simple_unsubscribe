django-simple_unsubscribe
=========================

A pluggable django app that prevents email delivery to un-desiring recipients.

This app was designed to be easily plugged into older django sites, with little configuration or adjustment. It works by monkey_patching django's email delivery classes, adding a blacklist check, and appending unsubscribe test to the end of every email.


Integration
-----------

1. Copy the 'unsubscribe' folder to your python working directory
2. Add 'unsubscribe' as the FIRST ITEM in you INSTALLED_APPS
3. Add to your urls.py: `url(r'^unsub/', include('unsubscribe.urls')),`
4. That's it.


Settings
--------

Ensure that the following settings are currently used:
settings.ROOT_DOMAIN


TODO:
-----

- Use django's 'sites' app to determin the domain, and site name.
- Use settings to provide the business address, and phone number.
