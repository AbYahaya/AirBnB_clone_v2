#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Ab Yahaya
"""
from fabric.api import local, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['100.26.220.103', '3.83.253.195']


def do_pack():
    """
    Targging project directory into a packages as .tgz
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None
