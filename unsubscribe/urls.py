from django.conf.urls import patterns, include, url

urlpatterns = patterns('unsubscribe.views',
    url(r'^(?P<token>[a-z0-9]+)/$', 'unsubscribe', name='unsubscribe'),
    url(r'^(?P<token>[a-z0-9]+)/complete/$', 'unsubscribe_complete', name='unsubscribe_complete'),
    url(r'^restore/(?P<token>[a-z0-9]+)/$', 'resubscribe', name='resubscribe'),
    url(r'^restore/(?P<token>[a-z0-9]+)/complete/$', 'resubscribe_complete', name='resubscribe_complete'),
)
