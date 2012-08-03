import webob.exc

from quantum.api.v2 import resource
from quantum.extensions import extensions
from quantum import wsgi


class PortForwardController(object):
    """
    """
    def _get_resource(self, request, id):
        """Lookup up the resource and verify ownership."""
        resource = None
        # find resource by id
        # if we can't find it raise
        #raise webob.exc.HTTPNotFound()

        # if request.context.tenant_id != resource.tenant_id:
        #    raise webob.exc.HTTPNotAuthorized()
        return resource

    def index(self, request):
        return {'portforwards': []} # return forwarded ports

    def create(self, request, body={}):
        input_body = request.json
        # validate and process incoming json dict
        # return new model with UUID
        fake_model = dict(id=id, destination='192.168.1.1/24', port=22)
        return {'portforward': fake_model}

    def show(self, request, id):
        return {'portforward': self._get_resource(request, id)}

    def update(self, request, id=None, body={}):
        resource = self._get_resource(request, id)
        # TODO: validate the body and update the resource
        return {'portforward': resource}

    def delete(self, request, id):
        resource = self._get_resource(request, id)
        return None


class Portforward(object):
    """
    """
    def get_name(self):
        return "port forward"

    def get_alias(self):
        return "dhportforward"

    def get_description(self):
        return "A port forwarding extension"

    def get_namespace(self):
        return 'http://docs.dreamcompute.com/api/ext/v1.0'

    def get_updated(self):
        return "2012-08-02T16:00:00-05:00"

    def get_resources(self):
        return [extensions.ResourceExtension(
            'dhportforward',
            resource.Resource(PortForwardController()))]

    def get_actions(self):
        return []

    def get_request_extensions(self):
        return []
