#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
from os import path, makedirs

def do_pack():
    """ Fabric script that generates a .tgz archive from the contents of the web_static folder"""

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
