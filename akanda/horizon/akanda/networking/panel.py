from django.utils.translation import ugettext_lazy as _

import horizon

from akanda.horizon.akanda import dashboard


class AkandaNetworking(horizon.Panel):
    name = _("Akanda Networking")
    slug = "networking"


dashboard.Akanda.register(AkandaNetworking)
