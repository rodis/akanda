from django.utils.translation import ugettext_lazy as _

import horizon


class Akanda(horizon.Dashboard):
    name = _("Akanda")
    slug = "akanda"
    panels = ('alias', 'configuration', 'firewall', 'nat',
              'portforward', 'vpn', 'networking',)
    default_panel = ('alias')
    supports_tenants = True


horizon.register(Akanda)
