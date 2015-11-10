django-simple_unsubscribe
=========================

A pluggable django app that prevents email delivery to un-desiring recipients.

This app was designed to be easily plugged into older django sites with very little configuration or adjustment. It works by monkey_patching django's email delivery classes; adding a blacklist check, and adding a link to unsubscribe to the end of every email.


Integration
-----------

1. Install:
 - using pip: `pip install https://github.com/Litiks/django-simple_unsubscribe/archive/master.zip`
 - or: add to your requirements.txt: `-e git+https://github.com/Litiks/django-simple_unsubscribe.git#egg=django-simple_unsubscribe`
 - or: copy the 'unsubscribe' folder to your python working directory
2. Add 'unsubscribe' as the FIRST ITEM in your settings.INSTALLED_APPS
3. Add to your urls.py: `url(r'^unsub/', include('unsubscribe.urls')),`
4. That's it! You're done!


Settings
--------

The following (optional) settings are currently used:

- EMAIL_SIGNATURE = "Litiks\n422111 Concession 6 NDR\nElmwood On, Canada, N0G1S0\n1 289-812-3835"


TODO:
-----

- Correct the handling of mail delivery to multiple recipients.
