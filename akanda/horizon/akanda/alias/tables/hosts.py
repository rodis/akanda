from django.utils.translation import ugettext as _

from horizon import tables


class Delete(tables.DeleteAction):
    data_type_singular = _("Host")
    data_type_plural = _("Hosts")


class Create(tables.LinkAction):
    name = "create"
    verbose_name = _("Create Alias")
    url = "horizon:nova:networking:port:create_host_alias"
    classes = ("ajax-modal", "btn-create")


class Edit(tables.LinkAction):
    name = "edit_host"
    verbose_name = _("Edit Alias")
    url = "horizon:"
    classes = ("ajax-modal", "btn-edit")


class HostTable(tables.DataTable):
    alias_name = tables.Column('', verbose_name=_("Alias Name"))
    instances = tables.Column('', verbose_name=_("Instances"))

    class Meta:
        name = "hosts"
        verbose_name = _("Host Aliases")
        table_actions = (Create, Delete,)
        row_actions = (Edit,)
