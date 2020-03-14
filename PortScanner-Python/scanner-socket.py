#!/usr/bin/env python3

"""Simple network host port scanner.

Scans host for the open ports and saves them to a JSON file. Reruning
program shows only differences from the last scan.

Attributes:
    target (str): containing either single host or a network subnet

Example:
    $ scanner-socker.py 10.1.1.1
"""

import os
import sys
import socket
import ipaddress
import argparse


def scan_range(targets):
    """Scans list of IP addresses for any open ports.

    This is a simple TCP scanner using builtin socket library.

    Attributes:
        targets: list of IP addresses to scan

    Returns:
        list of tuples with scanned IPs and their open ports. Example:
        [
            ('10.1.1.1', [22, 25, 80]),
            ('10.1.1.2', [22])
        ]
    """
    res = []
    for host in targets:
        portlist = []
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Not doing full port scan, this is just to prove a point
        #for port in range(1, 1024):
        for port in range(7999, 8002):
            try:
                s.connect((host, port))
                portlist.append(port)
            except:
                continue

        res.append((host, portlist))

    return res



if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='Host or subnet port scanner')
    argparser.add_argument('target', help='host or network subnet to scan')
    args = argparser.parse_args()

    try:
        # Attempt to parse args as a single host IP
        targets = [str(ipaddress.ip_address(args.target))]
    except ValueError:
        try:
            # Attempt to parse args as a subnet range if failed, ignore host bits
            targets = [str(h) for h in ipaddress.ip_network(args.target, strict=False).hosts()]
        except ValueError:
            print('{} does not appear to be a valid IP address or network'.format(target), file=sys.stderr)
            sys.exit(1)

    print(scan_range(targets))
