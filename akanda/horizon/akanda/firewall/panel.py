from django.utils.translation import ugettext_lazy as _

import horizon

from akanda import dashboard


class Firewall(horizon.Panel):
    name = _("Firewall")
    slug = "firewall"


dashboard.Akanda.register(Firewall)
