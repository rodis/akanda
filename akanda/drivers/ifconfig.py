import re

import netaddr

from akanda import models
from akanda.drivers import base
from akanda.utils import execute


class InterfaceManager(base.Manager):
    """
    """
    EXECUTABLE = '/sbin/ifconfig'

    def get_interfaces(self, filters=None):
        return _parse_interfaces(self.do('-A'), filters=filters)

    def get_interface(self, ifname):
        output = self.do(ifname)
        return _parse_interfaces(self.do(ifname))[0]

    def update_interfaces(self, interfaces):
        for i in interfaces:
            self.update_interface(i)

    def up(self, interface):
        self.sudo(interface.name, 'up')

    def down(self, interface):
        self.sudo(interface.name, 'down')

    def update_interface(self, interface):
        old_interface = self.get_interface(interface.ifname)

        self._update_interface_description(interface)
        self._update_interface_groups(interface, old_interface)
        # Must update primary before aliases otherwise will lose address
        # in case where primary and alias are swapped.
        self._update_interface_primary_v4(interface, old_interface)
        self._update_interface_addresses(interface, old_interface)

    def _update_description(self, interface):
        self.sudo(interface.name, 'description', interface.description)

    def _update_groups(self, interface, old_interface):
        add = lambda g: ('group', g)
        delete = lambda g: ('-group', g)

        self._update_set(interface, old_interface, 'groups', add, delete)

    def _update_addresses(self, interface, old_interface):
        add = lambda a: (interface.ifname, 'alias',
                         str(a.ip), 'prefixlen', a.prefixlen)
        delete = lambda a: (interface.ifname, '-alias',
                         str(a.ip), 'prefixlen', a.prefixlen)

        self._update_set(interface, old_interface, 'addresses', add, delete)

    def _update_primary_v4(self, interface, old_interface):
        if interface.primary_v4 == old_interface.primary_v4:
            return

        if interface.primary_v4 is None:
            self.sudo(old_interface.primary_v4.ip,
                       'prefixlen',
                       interface.primary_v4.prefixlen,
                       'delete')
        else:
            self.sudo(interface.primary_v4.ip,
                       'prefixlen',
                       interface.primary_v4.prefixlen)

    def _update_set(self, interface, old_interface, attribute,
                    fmt_args_add, fmt_args_delete):

        next_set = set(getattr(interface, attrbute))
        prev_set = set(getattr(old_interface, attribute))

        if next_set == prev_set:
            return

        for item in (next_set - prev_set):
            self.sudo(fmt_args_add(item))

        for item in (prev_set - next_set):
            self.sudo(fmt_args_delete(item))


def _parse_interfaces(data, filters=None):
    retval = []
    for iface_data in re.split('(^|\n)(?=\w+\d{1,3}: flag)', data, re.M):
        if not iface_data.strip():
            continue

        for f in filters or ['']:
            if iface_data.startswith(f):
                break
        else:
            continue

        retval.append(_parse_interface(iface_data))
    return retval


def _parse_interface(data):
    retval = dict(addresses=[])
    for line in data.split('\n'):
        if line.startswith('\t'):
            line = line.strip()
            if line.startswith('inet'):
                retval['addresses'].append(_parse_inet(line))
            else:
                retval.update(_parse_other_params(line))
        else:
            retval.update(_parse_head(line))

    return models.Interface.from_dict(retval)


def _parse_head(line):
    retval = {}
    m = re.match(
            '(?P<ifname>\w*): flags=\d*<(?P<flags>[\w,]*)> mtu (?P<mtu>\d*)',
            line)
    if m:
        retval['ifname'] = m.group('ifname')
        retval['flags'] = m.group('flags').split(',')
        retval['mtu'] = int(m.group('mtu'))
    return retval


def _parse_inet(line):
    tokens = line.split()
    if tokens[0] == 'inet6':
        ip = tokens[1].split('%')[0]
        mask = tokens[3]
    else:
        ip = tokens[1]
        mask = str(netaddr.IPAddress(int(tokens[3], 16)))
    return netaddr.IPNetwork('%s/%s' % (ip, mask))


def _parse_other_params(line):
    if line.startswith('options'):
        m = re.match('options=[0-9a-f]*<(?P<options>[\w,]*)>', line)
        return m.groupdict()
    else:
        key, value = line.split(' ', 1)

        if key == 'ether':
            key = 'lladdr'
        elif key.endswith(':'):
            key = key[:-1]

        return [(key, value)]
