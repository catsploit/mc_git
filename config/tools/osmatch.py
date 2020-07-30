#!/usr/bin/python3
#-*- coding:utf-8 -*-

from config.functions import is_root
from config.colors import *
import nmap

class RootRequired(Exception): pass

def os_match(target, cmd_print=None):
    is_root()
    if is_root() != True:
        raise RootRequired("instruction require root priviliges for -sV & -O flags")

    Scanner = nmap.PortScanner()
    result = Scanner.scan(str(target), '25500-25565', '-sV -O')

    OS_LIST = Scanner[str(target)]['osmatch']
    chances = []
    for match in range(len(OS_LIST)):
        accuracy = Scanner[str(target)]['osmatch'][match]['osclass'][0]['accuracy']
        chances.append(int(accuracy))

    OS_CHOOSEN = max(chances)
    for chance in range(len(OS_LIST)):
        select = OS_LIST[chance]['osclass'][0]
        if select['accuracy'] == str(OS_CHOOSEN):
            osname = Scanner[str(target)]['osmatch'][chance]['name']
            cpe = OS_LIST[match]['osclass'][0]['cpe'][0].strip('cpe:/o:')
            break

    # - Print formatted results if it's enabled- #
    if cmd_print:
        os_format = """\
{3}{4}[-] {5}OS : {6}{0}
{3}{4}[-] {5}cpe : {6}{1}
{3}{4}[-] {5}chances : {6}{2}{5}%\n""".format(osname, cpe, OS_CHOOSEN, blue, bold, normal, red)
        print(os_format)

    os_results = {'osname': osname, 'cpe': cpe, 'accuracy': OS_CHOOSEN}
    return os_results
