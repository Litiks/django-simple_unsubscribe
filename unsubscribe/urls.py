from django.conf.urls import patterns, include, url

urlpatterns = patterns('unsubscribe.views',
    url(r'^(?P<token>.+?)/$', 'unsubscribe', name='unsubscribe'),
    url(r'^(?P<token>.+?)/complete/$', 'unsubscribe_complete', name='unsubscribe_complete'),
    url(r'^restore/(?P<token>.+?)/$', 'resubscribe', name='resubscribe'),
    url(r'^restore/(?P<token>.+?)/complete/$', 'resubscribe_complete', name='resubscribe_complete'),
)
