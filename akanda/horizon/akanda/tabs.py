from django.utils.translation import ugettext as _

from horizon import tabs


class AliasTab(tabs.Tab):
    name = _("Alias")
    slug = "alias"
    template_name = "akanda/simple.html"

    def get_context_data(self, request):
        return {}


class ConfigurationTab(tabs.Tab):
    name = _("Configuration")
    slug = "configuration"
    template_name = "akanda/simple.html"

    def get_context_data(self, request):
        return {}


class FirewallTab(tabs.Tab):
    name = _("Firewall")
    slug = "firewall"
    template_name = "akanda/simple.html"

    def get_context_data(self, request):
        return {}


class NatTab(tabs.Tab):
    name = _("Nat")
    slug = "nat"
    template_name = "akanda/simple.html"

    def get_context_data(self, request):
        return {}


class PortForwardTab(tabs.Tab):
    name = _("Port Forward")
    slug = "portforward"
    template_name = "akanda/simple.html"

    def get_context_data(self, request):
        return {}


class VPNTab(tabs.Tab):
    name = _("VPN")
    slug = "vpn"
    template_name = "akanda/simple.html"

    def get_context_data(self, request):
        return {}


class NetworkingTabs(tabs.TabGroup):
    slug = "networkingtabs"
    tabs = (AliasTab, ConfigurationTab, FirewallTab,
            NatTab, PortForwardTab, VPNTab)
