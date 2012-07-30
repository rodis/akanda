from django.utils.translation import ugettext_lazy as _

import horizon

from akanda.horizon.akanda import dashboard


class Portforward(horizon.Panel):
    name = _("Portforward")
    slug = "portforward"


dashboard.Akanda.register(Portforward)
