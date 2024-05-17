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
    """Fabric script that distributes an archive to your web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        # Extract the file name and remove the extension
        file_name = os.path.basename(archive_path)  # e.g., web_static_20170315003959.tgz
        file_name_no_ext = file_name.split('.')[0]  # e.g., web_static_20170315003959

        # Define the target paths
        tmp_path = '/tmp/{}'.format(file_name)
        release_path = "/data/web_static/releases/{}/".format(file_name_no_ext)

        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, tmp_path)

        # Create the release directory if it doesn't exist
        sudo("mkdir -p {}".format(release_path))

        # Uncompress the archive to the release directory
        sudo("tar -xzf {} -C {}".format(tmp_path, release_path))

        # Remove the uploaded archive from the /tmp/ directory
        sudo("rm {}".format(tmp_path))

        # Move files out of the web_static directory to the release path
        sudo("mv {0}/web_static/* {0}/".format(release_path))

        # Remove the now-empty web_static directory
        sudo("rm -rf {}/web_static".format(release_path))

        # Remove the current symbolic link
        sudo("rm -f /data/web_static/current")

        # Create a new symbolic link to the new release
        sudo("ln -s {} /data/web_static/current".format(release_path))

        return True
    except Exception as e:
        return False
