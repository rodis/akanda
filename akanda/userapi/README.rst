Akanda User-facing API implemented as a Quantum Extension
==========================================================

Portforward
-----------

portfoward.py implemented under quantum/extensions allows... 

Firewall
----------

firewall.py implemented under quantum/extensions allows...

AddressBook
---------
addressbook.py implemented under quantum/extensions allows...

Info
----

This is the home for the REST API that users will be calling directly with
their preferred REST tool (curl, Python wrapper, etc.).

This code will eventually become part of OpenStack or act as a source or
inspiration that will. As such, this API should be constructed entirely with
standard OpenStack tools.


Exploratory Dev Work
--------------------

You also have to update Quantum's policy file for the extension to work with
authZ.

    "create_portforward": [],
    "get_portforward": [["rule:admin_or_owner"]],
    "update_portforward": [["rule:admin_or_owner"]],
    "delete_portforward": [["rule:admin_or_owner"]]


If you want to use quotas:

add to the QUOTAS section of quantum.conf

quota_portforward = 10

=======

Installation - DevStack (single node setup)
------------

Preliminary steps:

1. Run ./stack.sh until the stack account and /opt/stack directory gets created.
2. Hit Ctrl+C
3. Create a localrc file with the following:

    MYSQL_PASSWORD=openstack
    RABBIT_PASSWORD=openstack
    SERVICE_TOKEN=openstack
    SERVICE_PASSWORD=openstack
    ADMIN_PASSWORD=openstack
                                                                                                                                                                                    idisable_service n-net
    enable_service q-svc
    enable_service q-agt
    enable_service q-dhcp
    enable_service quantum
    LIBVIRT_FIREWALL_DRIVER=nova.virt.firewall.NoopFirewallDriver
    Q_PLUGIN=openvswitch NOVA_USE_QUANTUM_API=v2


Quantum Extensions install:

1. Clone quantum to /opt/stack - git clone https://github.com/openstack/quantum.git
2. Copy db/models.py from userapi/db to quantum/db/models.py
3. Copy _authzbase.py userapi to quantum/extensions/
4. Copy portfoward.py userapi to quantum/extensions/
5. Copy firewally.py userapi to quantum/extensions/
6. Copy addressbook.py userapi to quantum/extensions/
7. Run ./stack.sh again to generate the required DB migrations and start services

To manually start and stop Quantum Services under DevStack:

1. Run 'screen -x'
2. Select q-svc. In most cases - Ctrl+A+1 should work.
3. Run the following to start Quantum or Ctrl+C to stop:

cd /opt/stack/quantum && python /opt/stack/quantum/bin/quantum-server
--config-file /etc/quantum/quantum.conf
--config-file /etc/quantum/plugins/openvswitch/ovs_quantum_plugin.ini


