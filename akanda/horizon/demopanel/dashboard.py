from django.utils.translation import ugettext_lazy as _

import horizon


class DemoPanelGroup(horizon.PanelGroup):
    name = _("Demo Panel")
    slug = "demopanel"
    panels = ("ovewview", "aliases", "nat", "portforward", "firewall",)


class DemoPanel(horizon.Dashboard):
    name = _("Admin")
    slug = "demopanel"
    panels = (DemoPanelGroup,)
    default_panel = "overview"
    roles = ("admin",)


horizon.register(DemoPanel)
