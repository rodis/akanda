import logging

from django.utils.translation import ugettext_lazy as _

from horizon import api, exceptions, forms, tables

from akanda.horizon.demopanel.aliases import forms, tables


LOG = logging.getLogger(__name__)


class IndexView(tables.DataTableView):
    table_class = tables.AdminImagesTable
    template_name = 'demopanel/templates/aliases/index.html'


class UpdateView(forms.XXX):
    template_name = 'demopanel/templates/aliases/update.html'
    form_class = forms.UpdateForm


class DetailView(xxx.XXX):
    """ Admin placeholder for image detail view. """
    pass
