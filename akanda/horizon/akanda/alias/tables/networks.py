from django.utils.translation import ugettext as _

from horizon import tables


class Delete(tables.DeleteAction):
    data_type_singular = _("Network")
    data_type_plural = _("Networks")


class Create(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Alias")
    url = "horizon:nova:networking:port:create_network_alias"
    classes = ("ajax-modal", "btn-create")


class Edit(tables.LinkAction):
    name = "edit"
    verbose_name = _("Edit Alias")
    url = "horizon:"
    classes = ("ajax-modal", "btn-edit")


class NetworkTable(tables.DataTable):
    tenant = tables.Column('', verbose_name=_("Alias Name"))
    cidr = tables.Column('', verbose_name=_("CIDR"))

    class Meta:
        name = "networks"
        verbose_name = _("Network Aliases")
        table_actions = (Create, Delete,)
        row_actions = (Edit,)
