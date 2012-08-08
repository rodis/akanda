"""Blueprint for version 1 of API.
"""

import flask

from akanda.routerapi.drivers import base
from akanda.routerapi.drivers import ifconfig
from akanda.routerapi.drivers import pf

blueprint = flask.Blueprint('v1', __name__)


@blueprint.route('/')
def welcome():
    return 'Welcome to Akanda'


## APIs for working with system.


@blueprint.route('/system/interfaces')
def get_interfaces():
    return 'OpenBSD ifconfig -a'


## APIs for working with firewall.

pf_mgr = pf.PfManager()

@blueprint.route('/firewall/rules')
def get_rules():
    pass
