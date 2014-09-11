from datetime import datetime

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings

from unsubscribe.models import UnsubscribeDetail

def unsubscribe(request, token):
    detail = get_object_or_404(UnsubscribeDetail, token=token)
    detail.unsub_date = datetime.today()
    detail.save()

    return HttpResponse("<h1>Unsubscribe Successful</h1>The email <em>%s</em> will no longer receive emails from <b>%s</b>" % (detail.email, settings.ROOT_DOMAIN))

