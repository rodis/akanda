from quantum.api.v2 import attributes
from quantum.db import models_v2
from quantum.extensions import extensions

from akanda.userapi import _authzbase
from akanda.userapi.db import models


# XXX: I used Network as an existing model for testing.  Need to change to
# use an actual PortForward model.
#
# Duncan: cool, we'll get a PortForward model in place ASAP, so that this code
# can be updated to use it.


class PortforwardResource(_authzbase.ResourceDelegate):
    """
    This class is responsible for receiving REST requests and operating on the
    defined data model to create, update, or delete portforward-related data.
    """
    model = models.PortForward
    resource_name = 'portforward'
    collection_name = 'portforwards'

    ATTRIBUTE_MAP = {
        'id': {'allow_post': False, 'allow_put': False,
               'validate': {'type:regex': attributes.UUID_PATTERN},
               'is_visible': True},
        'name': {'allow_post': True, 'allow_put': True,
                 'default': '', 'is_visible': True},
        'tenant_id': {'allow_post': True, 'allow_put': False,
                      'required_by_policy': True,
                      'is_visible': True},
    }

    def make_dict(self, portforward):
        """
        Convert a portforward model object to a dictionary.
        """
        # XXX here's an example that is used for converting a network model to
        # a dictionary (delete this when the portforard conversion has been
        # implemented):
        #res = {'id': network['id'],
        #       'name': network['name'],
        #       'tenant_id': network['tenant_id'],
        #       'admin_state_up': network['admin_state_up'],
        #       'status': network['status'],
        #       'subnets': [subnet['id']
        #                   for subnet in network['subnets']]}
        return res

    def create(self, tenant_id, resource_dict):
        #import pdb;pdb.set_trace()
        return {}

    def update(self, tenant_id, resource, resource_dict):
        #import pdb;pdb.set_trace()
        return {}


_authzbase.register_quota('portforward', 'quota_portforward')


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
            _authzbase.create_extension(PortforwardResource()))]
            #_authzbase.ResourceController(PortforwardResource()))]

    def get_actions(self):
        return []

    def get_request_extensions(self):
        return []
