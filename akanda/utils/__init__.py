from json import JSONEncoder
import os
import shlex
import subprocess
import tempfile


def execute(args, root_helper=None):
    if root_helper:
        cmd = shlex.split(root_helper) + args
    else:
        cmd = args

    return subprocess.check_output(map(str, cmd))


def replace_file(file_name, data):
    """Replaces the contents of file_name with data in a safe manner.

    First write to a temp file and then rename. Since POSIX renames are
    atomic, the file is unlikely to be corrupted by competing writes.

    We create the tempfile on the same device to ensure that it can be renamed.
    """

    base_dir = os.path.dirname(os.path.abspath(file_name))
    tmp_file = tempfile.NamedTemporaryFile('w+', dir=base_dir, delete=False)
    tmp_file.write(data)
    tmp_file.close()
    os.chmod(tmp_file.name, 0644)
    os.rename(tmp_file.name, file_name)


class ModelSerializer(JSONEncoder):
    """
    """
    def default(self, obj):
        if isinstance(obj, set):
            obj = list(set)
        known_types = [list, dict, str, unicode, int, float, bool, type(None)]
        if isinstance(obj, known_types):
            return JSONEncoder.default(self, obj)
        raise ValueError("Type %s (%s) not serializable" % (
            type(obj), str(obj)))