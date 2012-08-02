from django.utils.translation import ugettext as _

from horizon import forms


class CreatePort(forms.SelfHandlingForm):
    name = forms.CharField(label=_("Name"),)
    protocol = forms.CharField(label=_("Protocol"))
    port_numbers = forms.CharField(label=_("Port Numbers"))

    def handle(self, request, data):
        pass


class CreateHost(forms.SelfHandlingForm):
    name = forms.CharField(label=_("Name"),)
    protocol = forms.CharField(label=_("Instances"))

    def handle(self, request, data):
        pass


class CreateNetwork(forms.SelfHandlingForm):
    name = forms.CharField(label=_("Name"),)
    cidr = forms.CharField(label=_("CIDR"))

    def handle(self, request, data):
        pass
