from django.utils.translation import ugettext_lazy as _

import horizon

from akanda import dashboard


class Configuration(horizon.Panel):
    name = _("Configuration")
    slug = "configuration"


dashboard.Akanda.register(Configuration)
