from akanda.testing.fakes.horizon.fake_backend import DictKvs
from akanda.testing.fakes.horizon import fake_data
from akanda.testing.fakes.horizon import fake_backend


PORT_ALIASES_DB = DictKvs(fake_data.port_aliases_fake_data)
PortAliasManager = fake_backend.PortAliasManager(PORT_ALIASES_DB)


INSTANCES_FAKE_DATA = [(k, v['name']) for k, v in \
                       fake_data.instances_fake_data.items()]


HOST_ALIAS_DB = DictKvs(fake_data.host_aliases_fake_data)
HostAliasManager = fake_backend.HostAliasManager(HOST_ALIAS_DB)


NETWORK_ALIASES_DB = DictKvs(fake_data.network_aliases_fake_data)
NetworkAliasManager = fake_backend.NetworkAliasManager(NETWORK_ALIASES_DB)
