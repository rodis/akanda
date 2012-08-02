from django.utils.translation import ugettext as _

from horizon import tabs

from akanda.horizon.akanda.firewall.tables import FirewallTable


class FirewallTab(tabs.TableTab):
    name = _("Firewall")
    slug = "firewall_tab"
    table_classes = (FirewallTable,)
    template_name = "horizon/common/_detail_table.html"

    def get_firewall_data(self):
        return {}
