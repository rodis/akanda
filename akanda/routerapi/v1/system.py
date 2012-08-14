"""
Blueprint for the "system" portion of the version 1 of the API.
"""
import json
import logging

from flask import Response

from akanda import utils
from akanda.routerapi.drivers import ifconfig
from akanda.routerapi.drivers import pf


system = utils.blueprint_factory(__name__)
@system.route('/check_route')
def check_route():
    return Response("you got it! *** " + __name__ + " *** " + __file__)


@system.route('/interface/<ifname>')
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


@system.route('/interfaces')
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
