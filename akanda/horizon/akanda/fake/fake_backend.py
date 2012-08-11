from akanda.horizon.akanda.fake.fake_models import Port


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


class PortAliasManager(Manager):

    def list_all(self, request):
        return [Port(**v) for v in self.db.values()]
