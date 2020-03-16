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
import json

from collections import OrderedDict


def scan_range(targets):
    """Scans list of IP addresses for any open ports.

    This is a simple TCP scanner using builtin socket library.

    Attributes:
        targets (list): list of IP addresses to scan

    Returns:
        dictionary with scanned IPs and their open ports. Example:
        {
            '10.1.1.1': [22, 25, 80],
            '10.1.1.2': [22]
        }
    """
    res = OrderedDict([])
    for host in targets:
        portlist = []
        for port in range(1, 65535):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                portlist.append(port)
            except:
                continue

        res[host] = portlist

    return res


def compare_scans(newscan, oldscan={}):
    """Compares difference between subsequent scans.

    Check if there are results unique to the current scan when compared
    to the previous scan.

    Attributes:
        newscan (dict): dictionary of ip=ports mappings found in scan
        oldscan (dict): result of the previous scan

    Returns:
        list with only newly discovered changes:
        [
            (
                host,       # IP of the scanned host
                [ports],    # list of unique ports found in this scan
                False       # if there are any changes to open ports
            )
        ]
    """
    difference = []
    change = False
    for host, ports in list(newscan.items()):
        if host not in list(oldscan.keys()):
            change = True
        else:
            if sorted(ports) != sorted(oldscan[host]):
                change = True

        difference.append((host, ports, change))

    return difference



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

    # scan hosts for open ports
    scan = scan_range(targets)
    print(scan)

    oldscan = {}
    scan_store = './.scanresult.json'
    # check if there are any results of previous scan
    if os.path.exists(scan_store):
        with open(scan_store, 'r') as f:
            oldscan = json.load(f)

    # detect changes since last scan
    diff = compare_scans(scan, oldscan)

    # save the result of this scan
    with open(scan_store, 'w') as f:
        json.dump(scan, f)

    # Format and print results
    for host, ports, changed in diff:
        if changed:
            print('*Target - {}: Full scan results:*'.format(host))
            for port in ports:
                print('Host: {}    Ports: {}/open/tcp////'.format(host, port))
        else:
            print('*Target - {}: No new records found in the last scan.*'.format(host))
