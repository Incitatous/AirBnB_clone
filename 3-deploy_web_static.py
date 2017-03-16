#!/usr/bin/python3
from datetime import datetime
from fabric.api import run, put, sudo, local, env
from os.path import isfile


env.hosts = ['54.164.203.121', '54.152.248.231']
env.user = 'ubuntu'


def do_pack():
    """
    Sets up a server
    """
    fileName = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    local('tar -cvzf "versions/web_static_%s.tgz" ./web_static' % fileName)
    return ("versions/web_static_%s.tgz" % fileName)


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not isfile(archive_path):
        return False
    try:
        cleanArchive = archive_path.split("/")[-1]
        noExt = cleanArchive.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        sudo("mkdir -p {}{}".format(path, noExt))
        sudo("tar -xzf /tmp/{} -C {}{}".format(cleanArchive, path, noExt))
        sudo("rm /tmp/{}".format(cleanArchive))
        sudo("mv {}{}/web_static/* {}{}".format(path, noExt, path, noExt))
        sudo("rm -rf {}{}/web_static".format(path, noExt))
        sudo("rm /data/web_static/current")
        sudo("ln -s {}{} /data/web_static/current".format(path, noExt))
        return True
    except Exception:
        return False


def deploy():
    """
    Runs do_deploy & do_pack
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    else:
        return (do_deploy(archive_path))
