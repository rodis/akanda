from django.core.urlresolvers import reverse_lazy

from horizon import forms

from akanda.horizon.akanda.firewall.forms import CreateFirewallRule


class CreateFirewallRuleView(forms.ModalFormView):
    form_class = CreateFirewallRule
    template_name = 'akanda/firewall/create.html'
    success_url = reverse_lazy('horizon')
