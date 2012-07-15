import re
import subprocess

from akanda.drivers import base
from akanda.utils import execute


class InterfaceManager(base.Manager):
    EXECUTABLE = '/sbin/ifconfig'
    def get_interfaces(self, filters=None):
        return _parse_interfaces(self.do('-a'), filters=filters)

    def get_interface(self, ifname):
        output = self.do(ifname)
        return _parse_interfaces(self.do(ifname))[0]

    def update_interfaces(self, interfaces):
        for i in interfaces:
            self.update_interface(i)

    def update_interface(self, interface):
        old_interface = self.get_interface(interface.ifname)

        self._update_interface_description(interface)
        self._update_interface_groups(interface, old_interface)
        # Must update primary before aliases otherwise will lose address
        # in case where primary and alias are swapped.
        self._update_interface_primary_v4(interface, old_interface)
        self._update_interface_addresses(interface, old_interface)

    def _update_description(self, interface):
        self._sudo(interface.name, 'description', interface.description)

    def _update_groups(self, interface, old_interface):
        add = lambda g: ('group', g)
        delete = lambda g: ('-group', g)

        self._update_set(interface, old_interface, 'groups', add, delete)

    def _update_addresses(self, interface, old_interface):
        add = lambda a: (interface.ifname, 'alias',
                         str(a.ip), 'prefixlen', a.prefixlen)
        delete = lambda a: (interface.ifname, '-alias',
                         str(a.ip), 'prefixlen', a.prefixlen)

        self._update_set(interface, old_interface, 'addresses', add, delete,
                         netaddr.IPSet)

    def _update_primary_v4(self, interface, old_interface):
        if interface.primary_v4 == old_interface.primary_v4:
            return

        if interface.primary_v4 is None:
            self._sudo(old_interface.primary_v4.ip,
                       'prefixlen',
                       interface.primary_v4.prefixlen,
                       'delete')
        else:
            self._sudo(interface.primary_v4.ip,
                       'prefixlen',
                       interface.primary_v4.prefixlen)

    def _update_set(self, interface, old_interface, attribute,
                    fmt_args_add, fmt_args_delete, conversion_f=set):

        next_set = conversion_f(getattr(interface, attrbute))
        prev_set = conversion_f(getattr(old_interface, attribute))

        if next_set == prev_set:
            return

        for item in (next_set - prev_set):
            self._sudo(fmt_args_add(item))

        for item in (prev_set - next_set):
            self._sudo(fmt_args_delete(item))

def _parse_interfaces(data, filters=None):
    filter_re = '|'.join(filters or ['\w+'])
    iface_data = re.split('(^|\n)(?=\w+\d{1,3}: flag)', data, re.M)
    return [_parse_interface(i) for i in iface_data if i.strip()]



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

    return retval

def _parse_head(line):
    retval = {}
    m = re.match(
            '(?P<name>\w*): flags=\d*<(?P<flags>[\w,]*)> mtu (?P<mtu>\d*)',
            line)
    if m:
        retval['name'] = m.group('name')
        retval['flags'] = m.group('flags').split(',')
        retval['mtu'] = int(m.group('mtu'))
    return retval

def _parse_inet(line):
    tokens = line.split()

    if tokens[0] == 'inet6':
        prefixlen = tokens[3]
    else:
        prefixlen = 32
        test = 1
        mask = int(tokens[3], 16)
        while not (mask & test):
            prefixlen-=1
            test = test<<1

    return '%s/%s' % (tokens[1], prefixlen)

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

if __name__ == '__main__':
    import pprint
    pprint.pprint(InterfaceManager().get_interfaces())

