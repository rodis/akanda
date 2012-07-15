from akanda.utils import execute

class Manager(object):
    def __init__(self, root_helper='sudo'):
        self.root_helper = root_helper

    def sudo(self, *args):
        return execute([self.EXECUTABLE] + list(args), self.root_helper)

    def do(self, *args):
        return execute([self.EXECUTABLE] + list(args))
