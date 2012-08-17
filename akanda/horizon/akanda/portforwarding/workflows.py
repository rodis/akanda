from django.utils.translation import ugettext as _

from horizon import workflows
from horizon import forms
from horizon import exceptions

from akanda.horizon.akanda import common
from akanda.horizon.akanda.tabs import portforwarding_tab_redirect


TEST = (
    ('', ''),
    ('Custom', 'Custom'),
)


class DetailsAction(workflows.Action):
    rule_name = forms.CharField(label=_("Name"))
    instance = forms.ChoiceField(
        label=_("Instance"), choices=common.TEST_CHOICE)

    class Meta:
        name = _("Details")
        permissions = ()
        help_text = _("You can set up port forwarding rules here by picking "
                      "one of your instances, then which ports you want to "
                      "redirect.")


class Details(workflows.Step):
    action_class = DetailsAction
    contributes = ("rule_name", "instance")
    template_name = "akanda/portforwarding/_details_workflow_step.html"


class PortsAction(workflows.Action):
    public_ip = forms.CharField(label=_("Public Ip"))
    public_ip_port_alias = forms.ChoiceField(
        label=_("Port Alias"), choices=TEST)
    public_ip_protocol = forms.ChoiceField(
        label=_("Protocol"), choices=common.PROTOCOL_CHOICES)
    public_ip_ports = forms.CharField(label=_("Public Ports"))
    private_ip = forms.CharField(label=_("Private Ip"))
    private_ip_port_alias = forms.ChoiceField(
        label=_("Port Alias"), choices=TEST)
    private_ip_protocol = forms.ChoiceField(
        label=_("Protocol"), choices=common.PROTOCOL_CHOICES)
    private_ip_ports = forms.CharField(label=_("Public Ports"))

    class Meta:
        name = _("Ports")
        permissions = ()


class Ports(workflows.Step):
    action_class = PortsAction
    depends_on = ("rule_name", "instance")
    contributes = ("public_ip",
                   "public_ip_port_alias",
                   "public_ip_protocol",
                   "public_ip_ports",
                   "private_ip",
                   "private_ip_port_alias",
                   "private_ip_protocol",
                   "private_ip_ports")
    template_name = "akanda/portforwarding/_form_fields.html"


class PortForwardingRule(workflows.Workflow):
    slug = "create_portforwarding_rule"
    name = _("Create a Rule")
    finalize_button_name = _("Create Rule")
    success_message = _('Port Forwarding Rule successfully created')
    failure_message = _('Unable to create Port Forwarding Rule".')
    success_url = "horizon:nova:networking:index"
    default_steps = (Details, Ports)

    def get_success_url(self):
        url = super(PortForwardingRule, self).get_success_url()
        return "%s?tab=%s" % (url, portforwarding_tab_redirect())

    def handle(self, request, data):
        try:
            # port forwarding rule  creation goes here
            return True
        except:
            exceptions.handle(request)
            return False
