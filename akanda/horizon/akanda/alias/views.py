from django.core.urlresolvers import reverse_lazy

from horizon import forms

from .forms import CreatePort, CreateHost, CreateNetwork


class CreatePortView(forms.ModalFormView):
    form_class = CreatePort
    template_name = 'akanda/alias/port/create.html'
    success_url = reverse_lazy('horizon')


class CreateHostView(forms.ModalFormView):
    form_class = CreateHost
    template_name = 'akanda/alias/host/create.html'
    success_url = reverse_lazy('horizon')


class CreateNetworkView(forms.ModalFormView):
    form_class = CreateNetwork
    template_name = 'akanda/alias/network/create.html'
    success_url = reverse_lazy('horizon')
