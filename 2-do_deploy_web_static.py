#!/usr/bin/python3
from fabric.api import local, put, sudo, run, env
from datetime import datetime
from os import path, makedirs


env.hosts = ['100.26.210.165', '100.25.48.160']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """ Fabric script that distributes an archive to your web servers """

    if not path.exists(archive_path):
        return False

    # file_name = archive_path.split("/")[-1].strip(".tgz")
    file_name = path.basename(archive_path)
    no_exc = file_name.split('.')[0]
    uncompress_path = "/data/web_static/releases/{}".format(no_exc)

    tmp_path = '/tmp/{}'.format(file_name)
    try:
        upload = put(archive_path, tmp_path)
        sudo("mkdir -p {}".format(uncompress_path))
        sudo("tar -xvzf {} -C {}".format(tmp_path, uncompress_path))
        sudo("rm {}".format(tmp_path))
        sudo("mv {0}/web_static/* {0}/".format(uncompress_path))
        sudo("rm -rf {}/web_static".format(uncompress_path))
        sudo("rm -f /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(uncompress_path))
        return True
    except:
        return False
