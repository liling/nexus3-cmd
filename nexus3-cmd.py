#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nexus3 Command Line Client

Usage:

    nexus3-cmd command args

Commands:
    upload src dest		Upload file/dir to nexus3 raw repository

Options:
    -h, --help          Display this help and exit

The following environment variables are used to provide server
information: NEXUS_URL, NEXUS_USER, NEXUS_PASSWORD, NEXUS_REPO,
and they should be set.

"""

import getopt
import os
import sys
import logging
from nexuscli.nexus_config import NexusConfig
from nexuscli.nexus_client import NexusClient

class Nexus3Cmd:

    _url = None
    _user = None
    _password = None
    _repo = None
    _nexus_client = None

    def __init__(self):
        try:
            self._url = os.environ['NEXUS_URL']
            self._user = os.environ['NEXUS_USER']
            self._password = os.environ['NEXUS_PASSWORD']
            self._repo = os.environ['NEXUS_REPO']
        except KeyError:
            self.usage()

        nexus_config = NexusConfig(url=self._url, username=self._user, password=self._password)
        self._nexus_client = NexusClient(config=nexus_config)

    def usage(self, e=None):
        if e:
            print("Error:", e, file=sys.stderr)

        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)

    def run(self):

        try:
            opts, args = getopt.gnu_getopt(sys.argv[1:], "h")
        except getopt.GetoptError as e:
            self.usage(e)

        if len(args) <= 0:
            self.usage()

        cmd = args[0]
        if cmd == 'upload':
            self._upload(args, opts)
        else:
            usage()

    def _upload(self, args, opts):
        src = args[1]
        dest = args[2]

        repository = self._nexus_client.repositories.get_by_name(self._repo)
        if os.path.exists(src):

            destFull = "[%s] %s/%s" % (self._repo, dest, src)
            print("Upload %s to %s" % (src, destFull))

            if os.path.isdir(src):
                repository.upload_directory(src, dest)
            else:
                repository.upload_file(src, dest)
        else:
            print("%s not exists" % src, output=sys.stderr)	

if __name__ == '__main__':
    x = Nexus3Cmd()
    x.run()
