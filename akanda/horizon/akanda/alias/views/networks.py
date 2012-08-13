from django.core.urlresolvers import reverse_lazy

from horizon import forms

from akanda.horizon.akanda.alias.forms import CreateNetwork
from akanda.horizon.akanda.tabs import alias_tab_redirect


class CreateNetworkView(forms.ModalFormView):
    form_class = CreateNetwork
    template_name = 'akanda/alias/network/create.html'
    success_url = reverse_lazy('horizon:nova:networking:index')

    def get_success_url(self):
        url = super(CreateNetworkView, self).get_success_url()
        return "%s?tab=%s" % (url, alias_tab_redirect())
