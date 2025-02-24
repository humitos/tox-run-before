import pluggy
from os import system

hookimpl = pluggy.HookimplMarker("tox")

@hookimpl
def tox_before_run_commands(tox_env):
    for env in tox_env.conf.envlist:
        for cmd in tox_env.conf.envconfigs[env]._reader.getlist("run_before"):
            system(cmd)
