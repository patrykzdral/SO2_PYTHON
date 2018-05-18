#!/usr/bin/env python3
#
# Zadanie S1
# Patryk Zdral
# 18.05.2018 11:15 TP
#
#

import subprocess



def filter_ports_function(port_from=0, port_to=99999, return_port=False):
    stdoutdata = subprocess.getoutput("netstat -tulpn")
    list = stdoutdata.split()
    active_addresses_and_ports = ''
    ports = set()
    for i in range(0, len(list)):
        if (list[i] == '0.0.0.0:*' or list[i] == ':::*') and list[i + 1] != 'LISTEN':
            list.insert(i + 1, 'NOT LISTEN')

    for i in range(38, len(list), 7):
        if list[i + 5] == 'LISTEN':
            port = get_port(list[i + 3])
            if port_from <= port <= port_to:
                ports.add(port)
                active_addresses_and_ports += list[i + 3] + '\n'

    if return_port:
        return ports
    else:
        return active_addresses_and_ports


def get_port(var):
    concat = ''
    for c in reversed(var):
        if c == ":":
            return int(concat[::-1])
        else:
            concat += c
    return int(concat[::-1])


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 3:
        port_from = int(sys.argv[1])
        port_to = int(sys.argv[2])
    else:
        port_from = 0
        port_to = 99999
    print(filter_ports_function(port_from, port_to))
