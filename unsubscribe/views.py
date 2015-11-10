from datetime import datetime

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.sites.models import Site

from unsubscribe.models import UnsubscribeDetail

def unsubscribe(request, token, template_name='unsubscribe/complete.html'):
    detail = get_object_or_404(UnsubscribeDetail, token=token)
    detail.unsub_date = datetime.today()
    detail.save()

    site = Site.objects.get_current()

    context = {
        'unsubscribe_detail': detail,
        'site': site,
    }
    return render_to_response(template_name, RequestContext(request, context))
