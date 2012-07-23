from django.utils.translation import ugettext_lazy as _

import horizon

from akanda import dashboard


class Vpn(horizon.Panel):
    name = _("Vpn")
    slug = "vpn"


dashboard.Akanda.register(Vpn)
