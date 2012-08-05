"""Blueprint for version 1 of API.
"""
# Fix paths for imports for production deployment
import flask
from drivers import ifconfig
import utils


blueprint = flask.Blueprint('v1', __name__)


## APIs for working with system.


@blueprint.route('/get_interfaces')
def get_interfaces():
    return 'OpenBSD ifconfig -a'


## APIs for working with firewall.


@blueprint.route('/get_rules')
def get_rules():
    pass
