from akanda.horizon.akanda.common import PROTOCOL_CHOICES as protocol_choices


PROTOCOL_CHOICES = dict(protocol_choices)


class Port(object):

    def __init__(self, id, alias_name, protocol, ports):
        self.id = id
        self.alias_name = alias_name
        self._protocol = protocol
        self._ports = ports

    @property
    def protocol(self):
        return PROTOCOL_CHOICES[self._protocol]

    @protocol.setter
    def protocol(self, value):
        self._protocol = value

    @property
    def ports(self):
        return '-'.join(map(str, self._ports))

    @ports.setter
    def ports(self, value):
        return self._ports
