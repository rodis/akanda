from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from horizon import forms
from horizon import messages
from horizon import exceptions

from akanda.horizon.akanda import common
from akanda.horizon.akanda.tabs import alias_tab_redirect


class BasePortAliasForm(forms.SelfHandlingForm):
    id = forms.CharField(
        label=_("Id"), widget=forms.HiddenInput, required=False)
    alias_name = forms.CharField(label=_("Name"),)
    protocol = forms.ChoiceField(
        label=_("Protocol"), choices=common.PROTOCOL_CHOICES)
    ports = forms.CharField(label=_("Port Numbers"))


class CreatePortAliasForm(BasePortAliasForm):
    def handle(self, request, data):
        try:
            self._create_port_alias(request, data)
            messages.success(request,
                _('Successfully created port alias: %s') % data['alias_name'])
            return data
        except:
            redirect = "%s?tab=%s" % (
                reverse("horizon:nova:networking:index"), alias_tab_redirect())
            exceptions.handle(request, _('Unable to create port alias.'),
                              redirect=redirect)

    def _create_port_alias(self, request, data):
        from akanda.horizon.akanda.fake import PortAliasManager
        PortAliasManager.create(request, data)


class EditPortAliasForm(BasePortAliasForm):
    def handle(self, request, data):
        try:
            self._update_port_alias(request, data)
            messages.success(request,
                _('Successfully updated port alias: %s') % data['alias_name'])
            return data
        except:
            redirect = "%s?tab=%s" % (
                reverse("horizon:nova:networking:index"), alias_tab_redirect())
            exceptions.handle(request, _('Unable to create port alias.'),
                              redirect=redirect)

    def _update_port_alias(self, request, data):
        from akanda.horizon.akanda.fake import PortAliasManager
        PortAliasManager.update(self.request, data)