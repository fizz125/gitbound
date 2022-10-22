#!/bin/env python3

# GIB DIRETIDE ༼ つ ◕_◕ ༽つ

import argparse

from pathlib import Path
from git import Repo

from meta import *


def is_git_command(subc):
    return False


def run_command(subc, extra_args, metarepos, subrepos):

    # match only works in python 3.10
    match subc:
        case 'populate':
            pass
        case 'attach':
            pass
        case 'exec':
            pass
        case 'status':
            pass
        case _:
            if not is_git_command(subc):
                pass
            else:
                print("Error: invalid command")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='gitbound is an implementation of gitslave in python')

    parser.add_argument('--version', action='version', version='0.1')
    parser.add_argument('-p', '--parallel', help='Number of parallel threads', metavar='COUNT', required=False)
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Increase output', required=False)
    parser.add_argument('-q', '--quiet', action='store_true', help='Silent operation', required=False)
    parser.add_argument('-n', '--no-pager', action='store_true', help='Do not use pager', required=False)
    parser.add_argument('--paginate', action='store_true', help='???', required=False)
    parser.add_argument('--eval-args', action='store_true', help='???', required=False)
    parser.add_argument('--exclude', help='???', metavar='SUBREPO-REGEXP', required=False)
    parser.add_argument('--keep-going', action='store_true', help='Keep going even if error on a repo is encountered', required=False)
    parser.add_argument('--no-commit', action='store_true', help='???', required=False)
    parser.add_argument('--no-hide', action='store_true', help='???', required=False)
    parser.add_argument('--no-progress', action='store_true', help='???', required=False)
    parser.add_argument('--no-master', action='store_true', help='???', required=False)
    # --with-ifpreset|--just-ifpresent

    # gib specific subcommands
    subcommands = ['clone', 'prepare', 'attach', 'populate', 'release', 'detatch', \
            'pulls', 'logs', 'exec', 'resolve', 'update-remote-url', 'remote-add', 'statuses', 'archive']
    # git command that gib treats special
    subcommands += ['pull', 'push']
    # Regular git commands so that the parser doesn't choke
    subcommands += ['status']
    parser.add_argument('subcommand', help='gitbound subcommand', choices=subcommands, metavar='subcommand')

    #a parser.add_subparsers

    args = parser.parse_known_args()

    print("main args: ")
    print(args[0])
    print("remaining args:")
    print(args[1])


    # Initialize metarepo
    metarepo = get_metarepo()

    # Initialize subrepos
    subrepo_paths = parse_metafile()
    subrepos = {}

    for repopath in subrepo_paths:
        try:
           sr = Repo(Path.cwd() / repopath)
           subrepos[repopath] = sr
        except:
            print("Repo for {} not found".format(repopath))


    run_command(args[0].subcommand, args[1], metarepo, subrepos)
