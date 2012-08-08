"""Blueprint for version 1 of API.
"""

import flask

from akanda.routerapi.drivers import ifconfig

blueprint = flask.Blueprint('v1', __name__)


@blueprint.route('/')
def welcome():
    return 'Welcome to Akanda'


## APIs for working with system.


@blueprint.route('/system/interfaces')
def get_interfaces():
    return 'OpenBSD ifconfig -a'


## APIs for working with firewall.


@blueprint.route('/firewall/rules')
def get_rules():
    pass
