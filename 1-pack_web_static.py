#!/usr/bin/python3
# Fabric script that generates a .tgz archive.
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    try:
        os.makedirs("versions", exist_ok=True)
        
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        file = f"versions/web_static_{timestamp}.tgz"
        
        result = local(f"tar -cvzf {file} web_static", capture=True)
        
        if result.succeeded:
            return file
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
