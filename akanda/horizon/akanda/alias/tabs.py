from django.utils.translation import ugettext as _

from horizon import tabs

from akanda.horizon.akanda.alias.tables import (
    PortAliasTable, HostTable, NetworkTable)


class AliasTab(tabs.TableTab):
    name = _("Alias")
    slug = "alias_tab"
    table_classes = (PortAliasTable, HostTable, NetworkTable)
    template_name = "akanda/alias/index.html"
    # preload = False

    def get_ports_data(self):
        from akanda.horizon.akanda.fake import PortAliasManager
        return PortAliasManager.list_all(self.request)

    def get_hosts_data(self):
        from akanda.horizon.akanda.fake import HostAliasManager
        return HostAliasManager.list_all(self.request)

    def get_networks_data(self):
        return {}
