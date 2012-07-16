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
    def __init__(self, action=None, interface=None, family=None,
                 protocol=None, source=None, source_port=None,
                 destination_interface=None,
                 destination=None, destination_port=None,
                 redirect=None, redirect_port=None):

        self.action = action
        self.interface = interface
        self.family = family
        self.protocol = protocol
        self.from_table = from_table
        self.source = source
        self.source_port = source_port
        self.destination_interface = destination_interface
        self.destination = destination
        self.desination_port = destination_port
        self.redirect = redirect
        self.redirect_port = redirect_port

    def __setattribute__(self, name, value):
        if name != 'action' and not value:
            pass
        elif name == 'action':
            assert value in ('pass', 'block')
        elif name in ('source', 'desination'):
            if '/' in value:
                value = netaddr.IPNetwork(value)
        elif name == 'redirect':
            value = netaddr.IPNetwork(value)
        elif name.endswith('_port'):
            value = int(value)
        elif name == 'family':
            assert value in ('inet', 'inet6')
        elif name == 'protocol':
            assert value in ('tcp', 'udp', 'imcp')
        elif name == 'redirect':
            value = netaddr.IPAddress(redirect_port)

        super(FilterRule, self).__setattribute__(name, value)

    @property
    def pf_rule(self):
        retval = [self.action]
        if self.interface:
            retval.append('on %s' % self.interface)
        if self.family:
            retval.append(self.family)
        if self.protocol:
            retval.append('proto %s' % self.protocol)
        if self.source or self.source_port:
            retval.append('from')
            if self.source:
                retval.append(str(self.source))
            if self.source_port:
                retval.append('port %s' % self.source)
        if (self.destination_interface or self.destination or self.destinaton_port):
            retval.append('to')
            if self.destination_interface:
                retval.append(self.destination_interface)
            if self.destination:
                retval.append(str(self.destination))
            if self.destination_port:
                retval.append('port %s' % self.destination_port)
        if self.redirect:
            retval.append('rdr-to')
            retval.append(str(self.redirect))
            retval.append('port %s' % self.redirect_port)
        return  ' '.join(retval)

    @classmethod
    def from_dict(self, d):
        return FilterRule(**d)


class Anchor(object):
    def __init__(self, name, rules=[]):
        self.name = name
        self.rules = rules

    @property
    def pf_rule(self):
        pf_rules = '\n\t'.join([r.pf_rule for r in self.rule])
        return "anchor %s {\n%s\n}\n" % (self.name, pf_rules)

    def external_pf_rule(self, base_dir):
        path = os.path.abspath(os.path.join(base_dir, self.name))
        return 'anchor %s\nload anchor %s from %s' % (self.name,
                                                      self.name,
                                                      path)


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