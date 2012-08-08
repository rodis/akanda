"""Blueprint for version 1 of API.
"""

import flask
import json

from akanda import utils

from akanda.routerapi.drivers import base
from akanda.routerapi.drivers import ifconfig
from akanda.routerapi.drivers import pf

blueprint = flask.Blueprint('v1', __name__)


@blueprint.route('/')
def welcome():
    return 'Welcome to Akanda'


## APIs for working with system.

if_mgr = ifconfig.InterfaceManager()


@blueprint.route('/system/interfaces')
def get_interfaces():
    results = if_mgr.get_interfaces()
    interfaces = [x.to_dict() for x in results]
    return json.dumps({"interfaces": interfaces}, cls=utils.ModelSerializer)


## APIs for working with firewall.

pf_mgr = pf.PfManager()


@blueprint.route('/firewall/rules')
def get_rules():
    results = pf_mgr.get_rules()
    return results
