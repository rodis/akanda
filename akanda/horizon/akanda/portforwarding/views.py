from horizon import workflows

from akanda.horizon.akanda.portforwarding.workflows import PortForwardingRule


class CreatePortForwardingRuleView(workflows.WorkflowView):
    workflow_class = PortForwardingRule
    template_name = "nova/instances/launch.html"
