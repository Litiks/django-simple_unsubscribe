from datetime import datetime

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.conf import settings

from unsubscribe.models import UnsubscribeDetail

def unsubscribe(request, token):
    detail = get_object_or_404(UnsubscribeDetail, token=token)
    detail.unsub_date = datetime.today()
    detail.save()

    site = Site.objects.get_current()

    context = {
        'unsubscribe_detail': detail,
        'site': site,
    }

    # send a confirmation email
    message = render_to_string('unsubscribe/email/unsubscribe_complete.txt', context)
    # try
    html_message = render_to_string('unsubscribe/email/unsubscribe_complete.html', context)
    send_mail("You have unsubscribed", message, settings.DEFAULT_FROM_EMAIL, [detail.email,], html_message=html_message, bypass_unsub=True)

    return render_to_response(template_name, RequestContext(request, context))

def unsubscribe_complete(request, token, template_name='unsubscribe/unsubscribe_complete.html'):
    detail = get_object_or_404(UnsubscribeDetail, token=token)
    site = Site.objects.get_current()

    context = {
        'unsubscribe_detail': detail,
        'site': site,
    }
    return render_to_response(template_name, RequestContext(request, context))

def resubscribe(request, token):
    detail = get_object_or_404(UnsubscribeDetail, token=token)
    detail.unsub_date = None
    detail.save()

    site = Site.objects.get_current()

    context = {
        'unsubscribe_detail': detail,
        'site': site,
    }

    # send a confirmation email
    message = render_to_string('unsubscribe/email/resubscribe_complete.txt', context)
    # try
    html_message = render_to_string('unsubscribe/email/resubscribe_complete.html', context)
    send_mail("You have unsubscribed", message, settings.DEFAULT_FROM_EMAIL, [detail.email,], html_message=html_message, bypass_unsub=True)

    return render_to_response(template_name, RequestContext(request, context))

def resubscribe_complete(request, token, template_name='unsubscribe/resubscribe_complete.html'):
    detail = get_object_or_404(UnsubscribeDetail, token=token)
    site = Site.objects.get_current()

    context = {
        'unsubscribe_detail': detail,
        'site': site,
    }
    return render_to_response(template_name, RequestContext(request, context))

