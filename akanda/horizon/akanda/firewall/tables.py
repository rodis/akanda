from django.utils.translation import ugettext as _

from horizon import tables


class DeleteFirewall(tables.DeleteAction):
    data_type_singular = _("Firewall")
    data_type_plural = _("Firewalls")


class CreateFirewall(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Firewall")
    url = "horizon:"
    classes = ("ajax-modal", "btn-create")


class FirewallTable(tables.DataTable):
    tenant = tables.Column('tenant_name', verbose_name=_("Tenant"))

    class Meta:
        name = "firewall"
        verbose_name = _("Firewall Rules")
        table_actions = (CreateFirewall, DeleteFirewall,)
