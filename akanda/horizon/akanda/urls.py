from django.conf.urls.defaults import patterns, url

from .views import IndexView

from akanda.horizon.akanda.alias.views import CreatePortView, CreateHostView, \
     CreateNetworkView
from akanda.horizon.akanda.firewall.views import CreateFirewallRuleView
from .portforwarding.views import CreatePortForwardingRuleView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    #
    url(r'^createport$', CreatePortView.as_view(),),
    url(r'^createhost$', CreateHostView.as_view(),),
    url(r'^createnetwork$', CreateNetworkView.as_view(),),
    #
    url(r'^createfirewallrule$', CreateFirewallRuleView.as_view(),),
    url(r'^createportforwardingrule$', CreatePortForwardingRuleView.as_view()),
)
