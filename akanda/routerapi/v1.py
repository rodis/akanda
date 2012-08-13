"""Blueprint for version 1 of API.
"""
import json
import logging

import flask
from flask import Response


from akanda import utils

from akanda.routerapi.drivers import ifconfig
from akanda.routerapi.drivers import pf

LOG = logging.getLogger(__name__)

blueprint = flask.Blueprint('v1', __name__)

#app = flask.Flask('akanda.routerapi')
#app.register_blueprint(blueprint, url_prefix='/v1')


@blueprint.before_request
def attach_config():
    #Use for attaching config prior to starting
    pass


@blueprint.route('/')
def welcome():
    '''
        Show welcome message
    '''
    return 'Welcome to the Akanda appliance'


#Write a separate decorator for all returning better jsonify to work with
#Akanda and Flask


## APIs for working with OpenBSD System.

if_mgr = ifconfig.InterfaceManager()


@blueprint.route('/system/interface/<ifname>')
def get_interface(ifname):
    '''
        Show interface parameters given an interface name.
        For example ge1, ge2 for generic ethernet
    '''
    result = if_mgr.get_interface(ifname)
    js = json.dumps({"interface": result.to_dict()}, cls=utils.ModelSerializer)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@blueprint.route('/system/interfaces')
def get_interfaces():
    '''
        Show all interfaces and parameters
    '''
    results = if_mgr.get_interfaces()
    interfaces = [x.to_dict() for x in results]
    js = json.dumps({"interfaces": interfaces}, cls=utils.ModelSerializer)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


## APIs for working with the Firewall.

pf_mgr = pf.PfManager()


@blueprint.route('/firewall/rules')
def get_rules():
    '''
        Show loaded firewall rules by pfctl
    '''
    results = pf_mgr.get_rules()
    return results


@blueprint.route('/firewall/states')
def get_states():
    '''
        Show firewall state table
    '''
    results = pf_mgr.get_states()
    return results


@blueprint.route('/firewall/anchors')
def get_anchors():
    '''
        Show loaded firewall anchors by pfctl
    '''
    results = pf_mgr.get_anchors()
    return results


@blueprint.route('/firewall/sources')
def get_sources():
    '''
        Show loaded firewall sources by pfctl
    '''
    results = pf_mgr.get_sources()
    return results


@blueprint.route('/firewall/info')
def get_info():
    '''
        Show verbose running firewall information
    '''
    results = pf_mgr.get_info()
    return results


@blueprint.route('/firewall/tables')
def get_tables():
    '''
        Show loaded firewall tables by pfctl
    '''
    results = pf_mgr.get_tables()
    return results


@blueprint.route('/firewall/labels')
def get_labels():
    '''
        Show loaded firewall labels by pfctl
    '''
    results = pf_mgr.get_labels()
    return results


@blueprint.route('/firewall/timeouts')
def get_timeouts():
    '''
        Show firewall connection timeouts
    '''
    results = pf_mgr.get_timeouts()
    return results


@blueprint.route('/firewall/memory')
def get_memory():
    '''
        Show firewall memory
    '''
    results = pf_mgr.get_memory()
    return results
