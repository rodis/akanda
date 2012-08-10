from akanda.horizon.akanda.fake.fake_backend import DictKvs
from akanda.horizon.akanda.fake import fake_data
from akanda.horizon.akanda.fake import fake_backend


PORT_ALIASES_DB = DictKvs(fake_data.port_aliases_fake_data)
PortAliasManager = fake_backend.PortAliasManager(PORT_ALIASES_DB)
