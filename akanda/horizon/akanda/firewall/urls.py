from django.conf.urls.defaults import patterns, url

from akanda.horizon.akanda.firewall.views import CreateFirewallRuleView

urlpatterns = patterns(
    '',
    url(r'create/$', CreateFirewallRuleView.as_view(), name='create'),
)
