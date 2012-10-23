from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _

from horizon import tables

from akanda.horizon.api import quantum_extensions_client


class Delete(tables.DeleteAction):
    name = 'delete'
    data_type_singular = _("Port Forward")
    data_type_plural = _("Ports Forward")
    success_url = reverse_lazy('horizon:nova:networking:index')

    # def get_success_url(self, request=None):
    #     return super(Delete, self).get_success_url(request)

    def delete(self, request, obj_id):
        quantum_extensions_client.portforward_delete(request, obj_id)


class Create(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Rule")
    url = "horizon:nova:networking:forwarding:create"
    classes = ("ajax-modal", "btn-create")


class Edit(tables.LinkAction):
    name = "edit_rule"
    verbose_name = _("Edit Rule")
    url = "horizon:nova:networking:forwarding:edit"
    classes = ("ajax-modal", "btn-edit")


class PortForwardingTable(tables.DataTable):
    rule_name = tables.Column('rule_name', verbose_name=_("Rule Name"))
    instances = tables.Column('display_instance', verbose_name=_("Instance"))
    public_port = tables.Column(
        'display_public_port', verbose_name=_("Public Port"))
    private_port = tables.Column(
        'display_private_port', verbose_name=_("Private Port"))

    class Meta:
        name = "portforwarding"
        verbose_name = _("Port Forwarding")
        table_actions = (Create, Delete,)
        row_actions = (Edit,)

    def get_object_display(self, datum):
        return datum.rule_name
