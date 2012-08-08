from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from horizon import forms
from horizon import messages
from horizon import exceptions

from akanda.horizon.akanda import common
from akanda.horizon.akanda.tabs import alias_tab_redirect


class CreatePort(forms.SelfHandlingForm):
    name = forms.CharField(label=_("Name"),)
    protocol = forms.ChoiceField(
        label=_("Protocol"), choices=common.PROTOCOL_CHOICES)
    port_numbers = forms.CharField(label=_("Port Numbers"))

    def handle(self, request, data):
        try:
            # port creation goes here
            messages.success(request, _('Successfully created port alias'))
                # _('Successfully created port alias: %s') % data['name'])
            return data
        except:
            redirect = "%s?tab=%s" % (
                reverse("horizon:nova:networking:index"),
                alias_tab_redirect())
            exceptions.handle(request, _('Unable to create port alias.'),
                              redirect=redirect)


class CreateHost(forms.SelfHandlingForm):
    name = forms.CharField(label=_("Name"),)
    instaces = forms.MultipleChoiceField(
        label=_("Instances"), choices=common.TEST_CHOICE)

    def handle(self, request, data):
        try:
            # port creation goes here
            messages.success(request, _('Successfully created host alias'))
                # _('Successfully created port alias: %s') % data['name'])
            return data
        except:
            redirect = "%s?tab=%s" % (
                reverse("horizon:nova:networking:index"),
                alias_tab_redirect())
            exceptions.handle(request, _('Unable to create host alias.'),
                              redirect=redirect)


class CreateNetwork(forms.SelfHandlingForm):
    name = forms.CharField(label=_("Name"),)
    cidr = forms.CharField(label=_("CIDR"))

    def handle(self, request, data):
        try:
            # port creation goes here
            messages.success(request, _('Successfully created network alias'))
                # _('Successfully created port alias: %s') % data['name'])
            return data
        except:
            redirect = "%s?tab=%s" % (
                reverse("horizon:nova:networking:index"),
                alias_tab_redirect())
            exceptions.handle(request, _('Unable to create network alias.'),
                              redirect=redirect)
