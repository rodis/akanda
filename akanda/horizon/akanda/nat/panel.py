from django.utils.translation import ugettext_lazy as _

import horizon

from akanda import dashboard


class Nat(horizon.Panel):
    name = _("Nat")
    slug = "nat"


dashboard.Akanda.register(Nat)
