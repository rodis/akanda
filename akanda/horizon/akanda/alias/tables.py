from django.utils.translation import ugettext as _

from horizon import tables


class DeletePort(tables.DeleteAction):
    name = 'delete'
    data_type_singular = _("Port Alias")
    data_type_plural = _("Port Aliases")

    def delete(self, request, obj_id):
        from akanda.horizon.akanda.fake import PortAliasManager
        PortAliasManager.delete(request, obj_id)


class CreatePort(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Alias")
    url = "horizon:nova:networking:port:create_port_alias"
    classes = ("ajax-modal", "btn-create")


class EditPort(tables.LinkAction):
    name = "edit_port"
    verbose_name = _("Edit Alias")
    url = "horizon:nova:networking:port:delete_port_alias"
    classes = ("ajax-modal", "btn-edit")


class PortTable(tables.DataTable):
    alias_name = tables.Column('alias_name', verbose_name=_("Alias Name"))
    protocol = tables.Column('protocol', verbose_name=_("Protocol"))
    ports = tables.Column('ports', verbose_name=_("Ports"))

    class Meta:
        name = "port"
        verbose_name = _("Port Aliases")
        table_actions = (CreatePort, DeletePort,)
        row_actions = (EditPort,)

    def get_object_display(self, datum):
        return datum.alias_name


class DeleteHost(tables.DeleteAction):
    data_type_singular = _("Host")
    data_type_plural = _("Hosts")


class CreateHost(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Alias")
    url = "horizon:nova:networking:port:create_host_alias"
    classes = ("ajax-modal", "btn-create")


class EditHost(tables.LinkAction):
    name = "edit_host"
    verbose_name = _("Edit Alias")
    url = "horizon:"
    classes = ("ajax-modal", "btn-edit")


class HostTable(tables.DataTable):
    alias_name = tables.Column('', verbose_name=_("Alias Name"))
    instances = tables.Column('', verbose_name=_("Instances"))

    class Meta:
        name = "host"
        verbose_name = _("Host Aliases")
        table_actions = (CreateHost, DeleteHost,)
        row_actions = (EditHost,)


class DeleteNetwork(tables.DeleteAction):
    data_type_singular = _("Network")
    data_type_plural = _("Networks")


class CreateNetwork(tables.LinkAction):
    name = "createnetwork"
    verbose_name = _("Create Alias")
    url = "horizon:nova:networking:port:create_network_alias"
    classes = ("ajax-modal", "btn-create")


class EditNetwork(tables.LinkAction):
    name = "edit_network"
    verbose_name = _("Edit Alias")
    url = "horizon:"
    classes = ("ajax-modal", "btn-edit")


class NetworkTable(tables.DataTable):
    tenant = tables.Column('', verbose_name=_("Alias Name"))
    cidr = tables.Column('', verbose_name=_("CIDR"))

    class Meta:
        name = "network"
        verbose_name = _("Network Aliases")
        table_actions = (CreateNetwork, DeleteNetwork,)
        row_actions = (EditNetwork,)
