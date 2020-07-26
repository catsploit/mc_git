#!/usr/bin/python3
#-*- coding:utf-8 -*-

import nmap
from config.functions import is_root
from config.tools import host_geo
from config.colors import *

class RootRequired(Exception): pass

def getEnvironment(parameters):
    ip = parameters[0]
    flag = None

    if len(parameters) > 1:
        flag = parameters[1]

    if is_root() != True:
        raise RootRequired("instruction require root priviliges for -sV & -O flags")

    Scanner = nmap.PortScanner()
    result = Scanner.scan(str(ip), '25500-25565', '-sV -O' )

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

    print(f"{red}{bold}{os_string}")
    if flag == '-out':
        import time
        filename = time.strftime('%X')

        with open(f'environment_report_{filename}.txt', 'a') as file:
            file.write(os_string)
            file.close()
