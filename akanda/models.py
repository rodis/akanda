import re

import netaddr

class Interface(object):
    def __init__(self, ifname=None, addresses=[], groups=None, flags=None,
                 lladdr=None, mtu=1500, media=None, primary_v4=None,
                 description=None, **extra_params):
        self.ifname = ifname
        self.description = description
        self.addresses = addresses
        self.groups = groups or []
        self.flags = flags or []
        self.mtu = mtu
        self.media = media
        self.primary_v4 = primary_v4
        self.extra_params = extra_params

    def __repr__(self):
        return '<Interface: %s %s>' % (self.ifname,
                                       [str(a) for a in self.addresses])

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value:
            self._description = ''
        elif re.match('\w*$', value):
            self._description = value
        else:
            raise ValueError, 'Description must be chars from [a-zA-Z0-9_]'

    @property
    def addresses(self):
        return self._addresses

    @addresses.setter
    def addresses(self, value):
        self._addresses = set([netaddr.IPNetwork(a) for a in value])

    @property
    def primary_v4(self):
        return self._primary_v4

    @primary_v4.setter
    def primary_v4(self, cidr):
        if cidr is None:
            self._primary_v4 = None
        else:
            cidr = netaddr.IPNetwork(cidr)
            self.addresses.add(cidr)
            self._primary_v4 = cidr

    @classmethod
    def from_dict(self, d):
        return Interface(**d)


class FilterRule(object):
    def __init__(self, action=None, interface=None, family=None, protocol=None,
                 from_cidr=None, from_port=None, to_cidr=None, to_port=None,
                 redirect=None, redirect_port=None):

        self.action = action
        self.interface = interface
        self.family = family
        self.protocol = protocol
        self.from_cidr = from_cidr
        self.from_port = from_port
        self.to_cidr = to_cidr
        self.to_port = to_port
        self.redirect = redirect
        self.redirect_port = redirect_port

    def __setattribute__(self, name, value):
        if name != 'action' and not value:
            pass
        elif name == 'action':
            assert value in ('pass', 'block')
        elif name in ('from_cidr', 'to_cidr', 'redirect'):
            value = netaddr.IPNetwork(value)
        elif name.endswith('_port'):
            value = int(value)
        elif name == 'family':
            assert value in ('inet', 'inet6')
        elif name == 'protocol':
            assert value in ('tcp', 'udp', 'imcp')

        super(FilterRule, self).__setattribute__(name, value)

    @classmethod
    def from_dict(self, d):
        return FilterRule(**d)


class AddressBookEntry(object):
    def __init__(self, name='', cidrs=[]):
        self.name = name
        self.cidrs = cidrs

    @property
    def cidrs(self):
        return self._cidrs

    @cidrs.setter
    def cidrs(self, values):
        self._cidrs = set([netaddr.IPNetwork(a) for a in values])


class Allocation(object):
    def __init__(self, lladdr, hostname, ip_address):
        self.lladdr = lladdr
        self.hostname = hostname
        self.ip_address = ip_address


class StaticRoute(object):
    def __init__(self, dest_cidr, next_hop):
        self.dest_cidr = dest_cidr
        self.next_hop = next_hop

    @property
    def dest_cidr(self):
        return self._dest_cidr

    @dest_cidr.setter
    def dest_cidr(self, value):
        self._dest_cidr = netaddr.IPNetwork(value)

    @property
    def next_hop(self):
        return self._next_hop

    @next_hop.setter
    def next_hop(self, value):
        self._next_hop = netaddr.IPAddress(value)
