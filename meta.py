
import re
import os

from pathlib import Path
from git import Repo

# Create meta repo object
#   if no meta repo preset, abort
#
# Find meta file
#   check for environment variable
#   check for gitslave env variable
#   check for default file name (.gitbind)
#   check for gitslave default file name (.gitslave)
# If no meta file found, abort
#
# Parse meta file to get repos
# (what to do about repos that don't exist?)
# Return object

def get_metarepo():
    try:
        return Repo(Path.cwd())
    except:
        print("Error. {} does not contain a git repo".format(Path.cwd()))

def get_metafile():
    metafile_names = [os.getenv('GITBIND'), os.getenv('GITSLAVE'), '.gitbind', '.gitslave']

    for fname in metafile_names:
        if fname is None:
            continue
        try:
            return open(fname)
        except:
            pass

    return None

def parse_metafile():
    repolist = {}
    repospec = re.compile(r"\"(\S+)\" \"(\S+)\"")
    try:
        with get_metafile() as f:
            for line in f:
                bind = re.match(repospec, line)
                repolist[bind.group(2)] = bind.group(1)
    except:
        pass

    return repolist
