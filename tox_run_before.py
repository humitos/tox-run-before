import pluggy
from os import system

hookimpl = pluggy.HookimplMarker("tox")

@hookimpl
def tox_configure(config):
    for env in config.envlist:
        for cmd in config.envconfigs[env]._reader.getlist("run_before"):
            system(cmd)
