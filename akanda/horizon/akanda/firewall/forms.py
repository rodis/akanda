from django.utils.translation import ugettext as _

from horizon import forms


class CreateFirewallRule(forms.SelfHandlingForm):
    source_network_alias = forms.CharField(label=_("Network Alias"),)
    source_cidr = forms.CharField(label=_("CIDR"),)
    source_port_alias = forms.CharField(label=_("Port Alias"),)
    source_protocol = forms.CharField(label=_("Protocol"),)
    source_public_ports = forms.CharField(label=_("Public Ports"),)
    destination_network_alias = forms.CharField(label=_("Network Alias"),)
    destination_cidr = forms.CharField(label=_("CIDR"),)
    destination_port_alias = forms.CharField(label=_("Port Alias"),)
    destination_protocol = forms.CharField(label=_("Protocol"),)
    destination_public_ports = forms.CharField(label=_("Public Ports"),)

    def handle(self, request, data):
        pass
