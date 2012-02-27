#!/usr/bin/env python
"""
Start a simple HTTP server, for simpler testing of AJAX calls, 
pathing of files and auto adding host name.
"""


import SimpleHTTPServer
import SocketServer
import threading
import webbrowser

standard_port = 8080
local_ip   = "127.0.0.1"

def open_browser(hostname, port):
 
    """Start a browser after waiting for half a second."""
    def _open_browser():
        webbrowser.open('http://%s:%s/' % (hostname, port))
    thread = threading.Timer(0.5, _open_browser)
    thread.start()

def add_host(hostname):
    """
        Add custom host to the hosts files
        Unix: /etc/hosts
    """

    import os
    with open("/etc/hosts", 'rt') as f:
        hosts = f.read()

        if hostname not in hosts:

            s = hosts + '\n' + '%s\t%s\n' % (local_ip, hostname)

            with open('/tmp/etc_hosts.tmp', 'wt') as outf:
                outf.write(s)

            os.system('sudo mv /tmp/etc_hosts.tmp /etc/hosts')


def start_server(hostname, port):
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", port), Handler)

    open_browser(hostname, port)

    print 'Serving at http://%s:%s/' % (hostname, port)
    httpd.serve_forever()

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(version='0.1', description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        '-p', 
        action="store", 
        dest="port",
        type=int, 
        default=standard_port,
        help='The port to use for the HTTP server')

    parser.add_argument(
        '-host', 
        action="store", 
        dest="hostname",
        type=str, 
        default=local_ip,
        help='Hostname alias')

    args = parser.parse_args()

    if args.hostname is not local_ip:
        add_host(args.hostname)
    
    start_server(args.hostname, args.port)
