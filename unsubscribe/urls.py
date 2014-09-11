from django.conf.urls.defaults import *

urlpatterns = patterns('unsubscribe.views',
    url(r'^(?P<token>.+)/$', 'unsubscribe', name='unsubscribe'),
)
