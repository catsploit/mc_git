#!/usr/bin/python3
#-*- coding:utf-8 -*-

import nmap
import time
from config.functions import is_root, cprint
from config.tools.host_geo import geolocate_host
from config.colors import *

class RootRequired(Exception): pass

def getEnvironment(parameters):
    ip = parameters[0]
    flag = None

    if len(parameters) > 1:
        flag = parameters[1]

    if is_root() != True:
        raise RootRequired("instruction require root priviliges for -sV & -O flags")

    cprint("[~] getenv >> Scanning target . . .", 'cyan', True)
    Scanner = nmap.PortScanner()
    result = Scanner.scan(str(ip), '25500-25565', '-sV -O' )

    # - OS MATCH - #
    OS_LIST = Scanner[str(ip)]['osmatch']
    chances = []
    for match in range(len(OS_LIST)):
        accuracy = Scanner[str(ip)]['osmatch'][match]['osclass'][0]['accuracy']
        chances.append(int(accuracy))

    OS_CHOOSEN = max(chances)
    for chance in range(len(OS_LIST)):
        select = OS_LIST[chance]['osclass'][0]
        if select['accuracy'] == str(OS_CHOOSEN):
            osname = Scanner[str(ip)]['osmatch'][chance]['name']
            cpe = OS_LIST[match]['osclass'][0]['cpe'][0].strip('cpe:/o:')
            break

    os_string = f"""
    I>>>>>>>>>>>>OS_MATCH RESULTS<<<<<<<<<<<<<I
    OS => {osname}
    CPE => {cpe}
    CHANCES => {OS_CHOOSEN}%
    I>>>>>>>>>>>>----------------<<<<<<<<<<<<<I\n"""

    cprint("[+] getenv >> MATCH! OS-scan results:", 'green', True)
    print(f"{red}{bold}{os_string}")

    # - geolocate host by ip-api - #
    cprint("[~] getenv >> geolocating target . . .", 'cyan', True)
    geolocate_result = geolocate_host(ip)
    cprint("[+] getenv >> Located\n", 'green', True)
    print(geolocate_result)

    if flag == '-out':
        filename = time.strftime('%X')

        with open(f'environment_report_{filename}.txt', 'a') as file:
            file.write(f"> ENVIRONMENT RESULTS FROM: '{ip}''" <\n')
            file.write(os_string + '\n')
            file.write("I>>>>>>>>>>>>GEOLOCATE_RESULTS<<<<<<<<<<<<<<I\n")
            geolocate_out = geolocate_result.strip("[0;36m").strip("")
            file.write(geolocate_out)
            file.write("I>>>>>>>>>>>>-----------------<<<<<<<<<<<<<<I\n")
            file.close()
