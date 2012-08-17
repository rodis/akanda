from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from horizon import forms
from horizon import messages
from horizon import exceptions

from akanda.horizon.akanda import common
from akanda.horizon.akanda.tabs import firewall_tab_redirect


POLICY_CHOICES = (
    (0, 'Allow'),
    (1, 'Deny'),
)

TEST = (
    ('', ''),
    ('Custom', 'Custom'),
)


class CreateFirewallRule(forms.SelfHandlingForm):
    source_network_alias = forms.ChoiceField(
        label=_("Network Alias"), choices=common.TEST_CHOICE)
    source_port_alias = forms.ChoiceField(
        label=_("Port Alias"), choices=TEST)
    source_protocol = forms.ChoiceField(
        label=_("Protocol"), choices=common.PROTOCOL_CHOICES)
    source_public_ports = forms.CharField(label=_("Public Ports"),)

    destination_network_alias = forms.ChoiceField(
        label=_("Network Alias"), choices=common.TEST_CHOICE)
    destination_port_alias = forms.ChoiceField(
        label=_("Port Alias"), choices=TEST)
    destination_protocol = forms.ChoiceField(
        label=_("Protocol"), choices=common.PROTOCOL_CHOICES)
    destination_public_ports = forms.CharField(label=_("Public Ports"),)

    policy = forms.ChoiceField(
        label=_("Policy"), choices=POLICY_CHOICES)

    def handle(self, request, data):
        try:
            # firewall rule  creation goes here
            messages.success(request, _('Successfully created firewall rule'))
                # _('Successfully created port alias: %s') % data['name'])
            return data
        except:
            redirect = "%s?tab=%s" % (
                reverse("horizon:nova:networking:index"),
                firewall_tab_redirect())
            exceptions.handle(request, _('Unable to create firewall rule.'),
                              redirect=redirect)
