#!/usr/bin/python3
from fabric.api import run, put, sudo
from fabric.api import env.hosts
from os.path import isfile

env.hosts = ['54.164.203.121', '54.152.248.231']


def do_deploy(archive_path):
    # if not isfile(archive_path):
        # return False
    try:
        isfile(archive_path)
        cleanArchive = archive_path.split("/")[-1]
        noExt = cleanArchive.split(".")[:1]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        sudo('mkdir -p %s%s' % path, noExt)
        sudo('tar -xzf %s -C %s%s' % cleanArchive, path, noExt)
        sudo('rm /tmp/%s' % cleanArchive)
        sudo('mv %s%s/web_static/* %s%s' % path, noExt, path, noExt)
        sudo('rm -rf %s%s/web_static' % path, noExt)
        sudo('rm /data/web_static/current')
        sudo('ln -s %s%s /data/web_static/current' % path, noExt)
        return True
    except Exception:
        return False
