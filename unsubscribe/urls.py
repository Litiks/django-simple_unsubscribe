from django.conf.urls import patterns, include, url

urlpatterns = patterns('unsubscribe.views',
    url(r'^(?P<token>.+)/$', 'unsubscribe', name='unsubscribe'),
)
