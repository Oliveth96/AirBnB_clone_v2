#!/usr/bin/python3
# A Fabric script that generates a .tgz archive from the contents of
# the web_static folder of my AirBnB Clone repo, using the function do_pack


from fabric.api import local
from datetime import datetime


def do_pack():
    """Pack web static directory"""
    dt = datetime.now()
    dt_str = dt.strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    path = 'versions/web_static_' + dt_str + '.tgz'
    tar = 'tar -cvzf {} web_static'.format(path)

    if local(tar):
        return None
    return path


if __name__ == '__main__':
    do_pack()
