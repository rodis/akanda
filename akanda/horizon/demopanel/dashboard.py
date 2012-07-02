from django.utils.translation import ugettext_lazy as _

import horizon


class DemoPanel(horizon.Dashboard):
    name = _("Demo Panel")
    slug = "demopanel"
    panels = ("overview", "services", "projects",)
    default_panel = "overview"
    roles = ("admin",)


horizon.register(DemoPanel)
