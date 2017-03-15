#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


def do_pack():
    fileName = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    local('tar -cvzf versions/"%s.tgz" web_static' % fileName)
