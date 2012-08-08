from django.core.urlresolvers import reverse_lazy

from horizon import forms

from akanda.horizon.akanda.tabs import firewall_tab_redirect
from akanda.horizon.akanda.firewall.forms import CreateFirewallRule


class CreateFirewallRuleView(forms.ModalFormView):
    form_class = CreateFirewallRule
    template_name = 'akanda/firewall/create.html'
    success_url = reverse_lazy('horizon:nova:networking:index')

    def get_success_url(self):
        url = super(CreateFirewallRuleView, self).get_success_url()
        return "%s?tab=%s" % (url, firewall_tab_redirect())
