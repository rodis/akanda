from django.utils.translation import ugettext_lazy as _

import horizon

from akanda.horizon.akanda import dashboard


class Alias(horizon.Panel):
    name = _("Alias")
    slug = "alias"


dashboard.Akanda.register(Alias)
