"""
cobbler daemon for logging remote syslog traffic during kickstart

Copyright 2007-2009, Red Hat, Inc and Others
Michael DeHaan <michael.dehaan AT gmail>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301  USA
"""

import sys
import time
import os
import binascii
import utils
import pwd

import api as cobbler_api
import remote


def main():
    core(logger=None)


def core(api):
    bootapi = api
    settings = bootapi.settings()
    xmlrpc_port = settings.xmlrpc_port

    regen_ss_file()
    do_xmlrpc_tasks(bootapi, settings, xmlrpc_port)


def regen_ss_file():
    # this is only used for Kerberos auth at the moment.
    # it identifies XMLRPC requests from Apache that have already
    # been cleared by Kerberos.
    ssfile = "/var/lib/cobbler/web.ss"
    fd = open("/dev/urandom")
    data = fd.read(512)
    fd.close()

    fd = os.open(ssfile, os.O_CREAT | os.O_RDWR, 0600)
    os.write(fd, binascii.hexlify(data))
    os.close(fd)

    http_user = "apache"
    if utils.check_dist() in ["debian", "ubuntu"]:
        http_user = "www-data"
    elif utils.check_dist() in ["suse", "opensuse"]:
        http_user = "wwwrun"
    elif os.path.exists("/etc/nginx/nginx.conf"):
        http_user = "nginx"
    os.lchown("/var/lib/cobbler/web.ss", pwd.getpwnam(http_user)[2], -1)

    return 1


def do_xmlrpc_tasks(bootapi, settings, xmlrpc_port):
    do_xmlrpc_rw(bootapi, settings, xmlrpc_port)


def log(logger, msg):
    if logger is not None:
        logger.info(msg)
    else:
        print >>sys.stderr, msg


def do_xmlrpc_rw(bootapi, settings, port):

    xinterface = remote.ProxiedXMLRPCInterface(bootapi, remote.CobblerXMLRPCInterface)
    server = remote.CobblerXMLRPCServer(('127.0.0.1', port))
    server.logRequests = 0      # don't print stuff
    xinterface.logger.debug("XMLRPC running on %s" % port)
    server.register_instance(xinterface)

    while True:
        try:
            print "SERVING!"
            server.serve_forever()
        except IOError:
            # interrupted? try to serve again
            time.sleep(0.5)


if __name__ == "__main__":
    bootapi = cobbler_api.BootAPI()
    settings = bootapi.settings()
    regen_ss_file()
    do_xmlrpc_rw(bootapi, settings, 25151)
