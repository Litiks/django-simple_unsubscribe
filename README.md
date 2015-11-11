django-simple_unsubscribe
=========================

A pluggable django app that prevents email delivery to un-desiring recipients.

This app was designed to be easily plugged into older django sites with very little configuration or adjustment. It works by monkey_patching django's email delivery classes; adding a blacklist check, and adding a link to unsubscribe to the end of every email.


Install
-------

- using pip: `pip install https://github.com/Litiks/django-simple_unsubscribe/archive/master.zip`
- or: add to your requirements.txt: `-e git+https://github.com/Litiks/django-simple_unsubscribe.git#egg=django-simple_unsubscribe`
- or: copy the 'unsubscribe' folder to your python working directory


Integrate
---------

1. Add 'unsubscribe' as the FIRST ITEM in your settings.INSTALLED_APPS
2. Add to your urls.py: `url(r'^unsub/', include('unsubscribe.urls')),`
3. run syncdb, or migrate (depending on your django version). `python manage.py migrate`
4. That's it! You're done!


Configure Templates
-------------------

Confirmation templates are shown on-screen when a user unsubscribes/resubscribes

- unsubscribe/unsubscribe_complete.html
- unsubscribe/resubscribe_complete.html


Email confirmation templates are sent via email when a user unsubscribes/resubscribes

- unsubscribe/email/unsubscribe_complete.txt
- unsubscribe/email/unsubscribe_complete.html
- unsubscribe/email/resubscribe_complete.txt
- unsubscribe/email/resubscribe_complete.html


According to canspam rules, your emails should include your address and a phone number. To add a 'signature' to all outgoing emails, create signature templates as follows:

- unsubscribe/email/signature.txt
- unsubscribe/email/signature.html


Usage
-----

Beyond setup, you won't need to make any changes to how you send emails. If you want, you can bypass the unsubscribe logic, (including the signature, and blacklist checks), just add `bypass_unsub=True` to your send_mail or EmailMessage call.


TODO:
-----

- Correct the handling of mail delivery to multiple recipients.
