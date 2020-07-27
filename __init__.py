#!/usr/bin/python3
#-*- coding:utf-8 -*-

from config.functions import cprint
from sys import exit

try:
    import nmap

except ImportError:
    exit(cprint("\n[!] ImportError >> python_nmap module is not installed\n", 'red', True))
