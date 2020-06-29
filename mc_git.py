#!/usr/bin/python3
#_*_ coding:utf8 _*_
	
from pkgutil import iter_modules
from config.functions import cprint
from config.functions import checking_packages

import sys
import socket
import os
import getpass
import requests
import json
import dns.resolver
import pip
import cmd

try:
	import nmap
except ImportError:
	sys.exit(cprint('\n[!] ImportError exception, please make sure that you have nmap\n', 'red'))


checking_packages()
