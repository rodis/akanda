from django.conf.urls.defaults import patterns, url

from akanda.horizon.demopanel.views import IndexView, CreateView


urlpatterns = patterns('akanda.horizon.demopanel.views',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^create/$', CreateView.as_view(), name='create'),
    url(r'^images/$', IndexView.as_view(), name='index'),
    url(r'^(?P<image_id>[^/]+)/update/$', UpdateView.as_view(), name='update'),
    url(r'^(?P<image_id>[^/]+)/detail/$', DetailView.as_view(), name='detail')
)
