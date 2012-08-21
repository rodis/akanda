from django.conf.urls.defaults import patterns, url

from akanda.horizon.akanda.portforwarding.views import (
    CreatePortForwardingRuleView)

urlpatterns = patterns(
    '',
    url(r'^create/$', CreatePortForwardingRuleView.as_view(), name='create'),
)
