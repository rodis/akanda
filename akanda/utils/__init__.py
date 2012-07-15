import shlex
import subprocess

def execute(args, root_helper=None):
    if root_helper:
        cmd = shlex.split(root_helper) + args
    else:
        cmd = args

    return subprocess.check_output(map(str, cmd))
