#!/usr/bin/python3
#-*- coding:utf-8 -*-

import nmap
from config.functions import is_root
class RootRequired(Exception): pass

def getEnvironment(ip):
    if is_root() != True:
        raise RootRequired("instruction require root priviliges for -sV & -O flags")

    Scanner = nmap.PortScanner()
    result = Scanner.scan(str(ip), '25500-25565', '-sV -O' )

    OS_LIST = Scanner[str(ip)]['osmatch']
    print(len(OS_LIST))

    # - OS MATCH PARSED BY NMAP - #
    for match in range(len(OS_LIST)):
        OS_TYPE = Scanner[str(ip)]['osmatch'][match]['osclass'][0]

        osname = Scanner[str(ip)]['osmatch']['name']
        accuracy = OS_TYPE['accuracy']
        cpe = OS_TYPE['cpe'].strip('cpe:/o:')

        print("\n<xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx>")
        print(f"OS #{match}:")
        print(f"NAME:{osfamily:>15}")
        print(f"PROBABILITY:{accuracy:>9}")
        print(f"CPE:{cpe:>16}")
        print("<xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx>\n")
