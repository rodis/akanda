from django.utils.translation import ugettext_lazy as _

import horizon


class Akanda(horizon.Dashboard):
    name = _("Akanda")
    slug = "akanda"
    panels = ()  # Add your panels here.
    default_panel = ''  # Specify the slug of the dashboard's default panel.


horizon.register(Akanda)
