from django.utils.translation import ugettext as _

from horizon import tables


class DeletePort(tables.DeleteAction):
    data_type_singular = _("Port")
    data_type_plural = _("Ports")


class CreatePort(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Port")
    url = "horizon:"
    classes = ("ajax-modal", "btn-create")


class PortTable(tables.DataTable):
    tenant = tables.Column('tenant_name', verbose_name=_("Tenant"))

    class Meta:
        name = "port"
        verbose_name = _("Port Aliases")
        table_actions = (CreatePort, DeletePort,)


class DeleteHost(tables.DeleteAction):
    data_type_singular = _("Host")
    data_type_plural = _("Hosts")


class CreateHost(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Host")
    url = "horizon:"
    classes = ("ajax-modal", "btn-create")


class HostTable(tables.DataTable):
    tenant = tables.Column('tenant_name', verbose_name=_("Tenant"))

    class Meta:
        name = "host"
        verbose_name = _("Host Aliases")
        table_actions = (CreateHost, DeleteHost,)


class DeleteNetwork(tables.DeleteAction):
    data_type_singular = _("Network")
    data_type_plural = _("Networks")


class CreateNetwork(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Network")
    url = "horizon:"
    classes = ("ajax-modal", "btn-create")


class NetworkTable(tables.DataTable):
    tenant = tables.Column('tenant_name', verbose_name=_("Tenant"))

    class Meta:
        name = "network"
        verbose_name = _("Network Aliases")
        table_actions = (CreateNetwork, DeleteNetwork,)
