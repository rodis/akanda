"""Blueprint for version 1 of API.
"""

import flask

from akanda.routerapi.drivers import ifconfig


blueprint = flask.Blueprint('v1', __name__)

app = flask.Flask('routerapi')
app.register_blueprint(blueprint, url_prefix='/v1')


@blueprint.before_request
def attach_config():
    #Use for attaching config prior to starting
    pass


@blueprint.route('/')
def welcome():
    return 'Welcome to Akanda'


## APIs for working with system.


@blueprint.route('/system/get_interfaces')
def get_interfaces():
    return 'OpenBSD ifconfig -a'


## APIs for working with firewall.


@blueprint.route('/firewall/get_rules')
def get_rules():
    pass
