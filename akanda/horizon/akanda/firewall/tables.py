from django.utils.translation import ugettext as _

from horizon import tables


class DeleteFirewallRule(tables.DeleteAction):
    data_type_singular = _("Firewall")
    data_type_plural = _("Firewalls")


class CreateFirewallRule(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Rule")
    url = "createfirewallrule"
    classes = ("ajax-modal", "btn-create")


class EditFirewallRule(tables.LinkAction):
    name = "edit_rule"
    verbose_name = _("Edit Rule")
    url = "horizon:"
    classes = ("ajax-modal", "btn-edit")


class FirewallTable(tables.DataTable):
    policy = tables.Column('', verbose_name=_("Policy"))
    source_ip = tables.Column('', verbose_name=_("Source IP"))
    source_ports = tables.Column('', verbose_name=_("Source Ports"))
    destination_ip = tables.Column('', verbose_name=_("Destionation Ip"))
    destination_ports = tables.Column('', verbose_name=_("Destionation Ports"))

    class Meta:
        name = "firewall"
        verbose_name = _("Firewall Rules")
        table_actions = (CreateFirewallRule, DeleteFirewallRule,)
        row_actions = (EditFirewallRule,)
