from django.conf.urls.defaults import patterns, url

from akanda.horizon.akanda.alias.views import (
    CreatePortAliasView, CreateHostAliasView, CreateNetworkView,
    EditPortAliasView, EditHostAliasView)


urlpatterns = patterns('',
    url(r'^port/create/$', CreatePortAliasView.as_view(),
        name='create_port_alias'),
    url(r'^host/create/$', CreateHostAliasView.as_view(),
        name='create_host_alias'),
    url(r'^network/create/$', CreateNetworkView.as_view(),
        name='create_network_alias'),
    url(r'^port/(?P<port_alias_id>[^/]+)/edit/$', EditPortAliasView.as_view(),
        name='edit_port_alias'),
    url(r'^host/(?P<host_alias_id>[^/]+)/edit/$', EditHostAliasView.as_view(),
        name='edit_host_alias'),
)
