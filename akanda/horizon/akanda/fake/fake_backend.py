from akanda.horizon.akanda.fake.fake_models import Port, Host


class DictKvs(dict):
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def set(self, key, value):
        if isinstance(value, dict):
            self[key] = value.copy()
        else:
            self[key] = value[:]

    def delete(self, key):
        del self[key]


class Manager(object):
    def __init__(self, db):
        self.db = db

    def delete(self, request, obj_id):
        del self.db[obj_id]

    def get(self, request, obj_id):
        return obj_id


class PortAliasManager(Manager):
    def list_all(self, request):
        return [Port(**v) for v in self.db.values()]

    def get(self, request, obj_id):
        # user = request.user
        # tenant_id = request.user.tenant_id
        return Port(**self.db[obj_id])

    def create(self, request, obj):
        obj = Port(**obj)
        self.db[obj.id] = obj.raw()

    def update(self, request, obj):
        obj = Port(**obj)
        self.db[obj.id] = obj.raw()


class HostAliasManager(Manager):
    def list_all(self, request):
        return [Host(**v) for v in self.db.values()]

    def get(self, request, obj_id):
        return Host(**self.db[obj_id])

    def create(self, request, obj):
        obj = Host(**obj)
        self.db[obj.id] = obj.raw()

    def update(self, request, obj):
        obj = Host(**obj)
        self.db[obj.id] = obj.raw()
