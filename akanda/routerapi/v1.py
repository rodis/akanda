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


@blueprint.route('/system/interface/<ifname>')
def get_interface(ifname):
    '''
        Show interface parameters given an interface name.
        For example ge1, ge2 for generic ethernet
    '''
    if_mgr = ifconfig.InterfaceManager()
    result = if_mgr.get_interface(ifname)
    js = json.dumps({"interface": result.to_dict()}, cls=utils.ModelSerializer)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


@blueprint.route('/system/interfaces')
def get_interfaces():
    '''
        Show all interfaces and parameters
    '''
    if_mgr = ifconfig.InterfaceManager()
    results = if_mgr.get_interfaces()
    interfaces = [x.to_dict() for x in results]
    js = json.dumps({"interfaces": interfaces}, cls=utils.ModelSerializer)
    resp = Response(js, status=200, mimetype='application/json')
    return resp


## APIs for working with the Firewall.


@blueprint.route('/firewall/rules')
def get_rules():
    '''
        Show loaded firewall rules by pfctl
    '''
    pf_mgr = pf.PfManager()
    results = pf_mgr.get_rules()
    return results


@blueprint.route('/firewall/states')
def get_states():
    '''
        Show firewall state table
    '''
    pf_mgr = pf.PfManager()
    results = pf_mgr.get_states()
    return results


@blueprint.route('/firewall/anchors')
def get_anchors():
    '''
        Show loaded firewall anchors by pfctl
    '''
    pf_mgr = pf.PfManager()
    results = pf_mgr.get_anchors()
    return results


@blueprint.route('/firewall/sources')
def get_sources():
    '''
        Show loaded firewall sources by pfctl
    '''
    pf_mgr = pf.PfManager()
    results = pf_mgr.get_sources()
    return results


@blueprint.route('/firewall/info')
def get_info():
    '''
        Show verbose running firewall information
    '''
    pf_mgr = pf.PfManager()
    results = pf_mgr.get_info()
    return results


@blueprint.route('/firewall/tables')
def get_tables():
    '''
        Show loaded firewall tables by pfctl
    '''
    pf_mgr = pf.PfManager()
    results = pf_mgr.get_tables()
    return results


@blueprint.route('/firewall/labels')
def get_labels():
    '''
        Show loaded firewall labels by pfctl
    '''
    pf_mgr = pf.PfManager()
    results = pf_mgr.get_labels()
    return results


@blueprint.route('/firewall/timeouts')
def get_timeouts():
    '''
        Show firewall connection timeouts
    '''
    pf_mgr = pf.PfManager()
    results = pf_mgr.get_timeouts()
    return results


@blueprint.route('/firewall/memory')
def get_memory():
    '''
        Show firewall memory
    '''
    pf_mgr = pf.PfManager()
    results = pf_mgr.get_memory()
    return results
