#!/usr/bin/python3
from fabric.api import run, put
from fabric.api import env.hosts
from os.path import isfile

env.hosts = ['54.164.203.121', '54.152.248.231']
def do_deploy(archive_path):
    isfile(archive_path)
    cleanArchive = archive_path.split("/")[-1]
    noExt = cleanArchive.split(".")[:1]
    put(archive_path, "/tmp/%s" % cleanArchive)
    run('mkdir -p /data/web_static/releases/%s' % noExt)
    run('tar -xzf archive_path -C /data/web_static/releases/%s' % noExt)
    run('rm /tmp/%s' % cleanArchive)
    run('mv /data/web_static/releases/%s/web_static/* /data/web_static/releases/%s' % noExt, noExt)
    run('rm -rf /data/web_static/releases/%s/web_static' % noExt)
    run('/data/web_static/current')
    run('ln -s /data/web_static/releases/%s /data/web_static/current' % noExt)
