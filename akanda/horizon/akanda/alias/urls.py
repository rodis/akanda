from django.conf.urls.defaults import patterns, url

from .views import CreatePortView, CreateHostView, CreateNetworkView


urlpatterns = patterns('',
    url(r'^port/create/$', CreatePortView.as_view(), name='create_port_alias'),
    url(r'^host/create/$', CreateHostView.as_view(), name='create_host_alias'),
    url(r'^network/create/$', CreateNetworkView.as_view(),
        name='create_network_alias'),
)
