from django.utils.translation import ugettext as _

from horizon import tables


class DeletePortForwardingRule(tables.DeleteAction):
    data_type_singular = _("Firewall")
    data_type_plural = _("Firewalls")


class CreatePortForwardingRule(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Rule")
    url = "horizon:nova:networking:forwarding:create_rule"
    classes = ("ajax-modal", "btn-create")


class EditPortForwardingRule(tables.LinkAction):
    name = "edit_rule"
    verbose_name = _("Edit Rule")
    url = "horizon:"
    classes = ("ajax-modal", "btn-edit")


class PortForwardingTable(tables.DataTable):
    rule_name = tables.Column('', verbose_name=_("Rule Name"))
    instance = tables.Column('', verbose_name=_("Instance"))
    public_ports = tables.Column('', verbose_name=_("Public Ports"))
    private_ports = tables.Column('', verbose_name=_("Private Ports"))

    class Meta:
        name = "portforwarding"
        verbose_name = _("Port Forwarding")
        table_actions = (CreatePortForwardingRule, DeletePortForwardingRule,)
        row_actions = (EditPortForwardingRule,)
