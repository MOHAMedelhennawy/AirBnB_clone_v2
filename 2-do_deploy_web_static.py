#!/usr/bin/python3
from fabric.api import local, put, sudo, run, env
from datetime import datetime
from os import path, makedirs


env.hosts = ['100.26.210.165', '100.25.48.160']
env.user = 'ubuntu'

def do_pack():
    """ Fabric script that generates a .tgz archive
    from the contents of the web_static folder"""

    date = datetime.now()
    archive_name = "web_static_{}".format(date.strftime("%Y%m%d%H%M%S"))
    archive_path = "versions/{}.tgz".format(archive_name)

    if not path.exists("versions"):
        makedirs("./versions")

    result = local("tar -cvzf {} web_static/".format(archive_path))
    if result.succeeded:
        return archive_path
    else:
        return None

def do_deploy(archive_path):
    """ Fabric script that distributes an archive to your web servers """

    # file_name = archive_path.split("/")[-1].strip(".tgz")
    file_name = path.basename(archive_path).split('.')[0]
    uncompress_path = "/data/web_static/releases/{}".format(file_name)

    if path.exists(archive_path):
        upload = put(archive_path, /tmp/)
        sudo("mkdir -p {}".format(uncompress_path))
        sudo("tar -xvzf /tmp/{} -C {}".format(archive_path, uncompress_path))
        sudo("rm -r /tmp/{}")
        sudo("unlink /data/web_static/current")
        sudo("ln -s /data/web_static/current {}".format(uncompress_path))
        return True
    else:
        return False
