from django.utils.translation import ugettext as _

from horizon import tabs

from akanda.horizon.akanda.alias.tables import PortTable, HostTable, \
     NetworkTable


class AliasTab(tabs.TableTab):
    name = _("Alias")
    slug = "alias_tab"
    table_classes = (PortTable, HostTable, NetworkTable)
    template_name = "akanda/alias/index.html"
    # preload = False

    def get_port_data(self):
        return {}

    def get_host_data(self):
        return {}

    def get_network_data(self):
        return {}
