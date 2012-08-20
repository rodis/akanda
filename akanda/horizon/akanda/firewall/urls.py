from django.conf.urls.defaults import patterns, url

from akanda.horizon.akanda.firewall.views import CreateFirewallRuleView

urlpatterns = patterns(
    '',
    url(r'^rule/create/$', CreateFirewallRuleView.as_view(),
        name='create_rule'),
)
