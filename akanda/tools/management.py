import sys

from akanda.drivers import ifconfig

def configure_management_interface():
    mgr = ifconfig.InterfaceManager()

    interfaces = mgr.get_interfaces(['em', 're'])
    interfaces.sort(key=lambda x:x.ifname)
    primary = interfaces[0]

    if not primary.is_up:
        mgr.up(primary)
        primary = mgr.get_interface(primary)

    for address in primary.addresses:
        if str(address.ip).startswith('fe80'):
            sys.stdout.write('%s%%%s\n' % (address.ip, primary.ifname))
            sys.exit()

    sys.stderr.write('Unable to bring up first interface (%s)!\n' %
                     primary.ifname)
