#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Ab Yahaya deploy static to server
"""
from fabric.api import local, put, run, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['54.224.18.138', '18.206.198.235']


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


def do_deploy(archive_path):
    """Deploy the boxing package tgz file
    """
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('Latest version deployed!')
        return True
    except:
        return False


def deploy():
    """
    A function to call do_pack and do_deploy
    """
    archive_path = do_pack()
    answer = do_deploy(archive_path)
    print('Latest version deployed to server')
    return answer
