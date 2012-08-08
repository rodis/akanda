from django.utils.translation import ugettext as _

from horizon import tabs

from akanda.horizon.akanda.firewall.tabs import FirewallTab
from akanda.horizon.akanda.alias.tabs import AliasTab
from akanda.horizon.akanda.portforwarding.tabs import PortForwardingTab


class ConfigurationTab(tabs.Tab):
    name = _("Configuration")
    slug = "configuration"
    template_name = "akanda/simple.html"

    def get_context_data(self, request):
        return {}


class NatTab(tabs.Tab):
    name = _("Nat")
    slug = "nat"
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
            NatTab, PortForwardingTab, VPNTab)


def alias_tab_redirect():
    tab_group_slug = NetworkingTabs.slug
    tab_slug = AliasTab.slug
    return "%s__%s" % (tab_group_slug, tab_slug)


def firewall_tab_redirect():
    tab_group_slug = NetworkingTabs.slug
    tab_slug = FirewallTab.slug
    return "%s__%s" % (tab_group_slug, tab_slug)


def portforwarding_tab_redirect():
    tab_group_slug = NetworkingTabs.slug
    tab_slug = PortForwardingTab.slug
    return "%s__%s" % (tab_group_slug, tab_slug)
