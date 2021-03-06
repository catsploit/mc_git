#!/usr/bin/python3
#-*- coding:utf-8 -*-

import nmap
import time
from config.functions import is_root
from config.tools.host_geo import geolocate_host
from config.tools.osmatch import os_match
from config.colors import *


def getEnvironment(parameters):
    ip = parameters[0]
    flag = None

    if len(parameters) > 1:
        flag = parameters[1]

    if is_root() != True:
        raise RootRequired("instruction require root priviliges for -sV & -O flags")

    print("{0}{1}[~] {0}getenv >> {1}Scanning target . . .".format(cyan, bold))
    Scanner = nmap.PortScanner()
    result = Scanner.scan(str(ip), '25500-25565', '-sV -O\n' )

    # - OS MATCH - #
    os_dict = os_match(ip)
    os_string = """{5}
---------OS_MATCH---------
{3}{4}[-] {5}OS : {6}{0}
{3}{4}[-] {5}CPE : {6}{1}
{3}{4}[-] {5}CHANCES : {6}{2}{5}%\n""".format(os_dict['osname'], os_dict['cpe'], os_dict['accuracy'], blue, bold, normal, red)

    # - Printing OS MATCH RESULTS - #
    print("{0}{1}[+] {0}getenv >> {1}MATCH!{0} OS-scan results:".format(green, bold))
    print(f"{os_string}")

    # - geolocate host by ip-api - #
    print("---------GEOLOCATE_RESULTS---------")
    print("{0}{1}[~] {0}getenv >> {1}geolocating target . . .".format(cyan, bold))
    geolocate_result = geolocate_host(ip)
    print("{0}{1}[+] {0}getenv >> {1}Located{0} - printing results\n".format(green, bold))
    print(geolocate_result)

    if flag == '-out':
        filename = time.strftime('%X')

        with open(f'environment_report_{filename}.txt', 'a') as file:
            file.write(f"> ENVIRONMENT RESULTS FROM: '{ip}'\n")
            file.write(os_string + '\n')
            geolocate_out = geolocate_result.strip("[0;36m").strip("")
            file.write(geolocate_out)
            file.close()
