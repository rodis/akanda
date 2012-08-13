import uuid

from akanda.horizon.akanda.common import PROTOCOL_CHOICES as protocol_choices
from akanda.horizon.akanda.fake.fake_data import instances_fake_data

PROTOCOL_CHOICES = dict(protocol_choices)


class Port(object):

    def __init__(self, alias_name, protocol, ports, id=None):
        self.alias_name = alias_name
        self.protocol = protocol
        self.ports = ports
        self.id = id or uuid.uuid4().hex

    @property
    def protocol(self):
        return PROTOCOL_CHOICES[self._protocol]

    @protocol.setter
    def protocol(self, value):
        if isinstance(value, basestring):
            self._protocol = int(value)
        else:
            self._protocol = value

    @property
    def ports(self):
        return '-'.join(map(str, self._ports))

    @ports.setter
    def ports(self, value):
        if isinstance(value, basestring):
            self._ports = map(int, value.split('-'))
            self._ports.sort()
        else:
            self._ports = value

    def raw(self):
        data = self.__dict__.copy()
        for k, v in data.items():
            if k.startswith('_'):
                tmp = data.pop(k)
                data[k[1:]] = tmp
        return data


class Host(object):

    def __init__(self, alias_name, instances, id=None):
        self.alias_name = alias_name
        self._instances = instances
        self.id = id or uuid.uuid4().hex

    @property
    def instances(self):
        instances = [instances_fake_data[instance]['name'] for instance in \
                     self._instances]
        instances.sort()
        return ', '.join(instances)

    def raw(self):
        data = self.__dict__.copy()
        for k, v in data.items():
            if k.startswith('_'):
                tmp = data.pop(k)
                data[k[1:]] = tmp
        return data

    def get_instances_list(self):
        return self._instances
