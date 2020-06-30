#!/usr/bin/python3
#_*_ coding:utf-8 _*_

import socket
import dns.resolver
from config.functions import cprint
from config.colors import *

def getbyhost(host):
	try:
		hostIP = socket.gethostbyname(host)
		return(print("{2}Done! {3}{0}{2} >> {3}{1}\n".format(host, hostIP, cyan, bold)))

	except socket.gaierror:
		return(cprint("[!] gethost >> Unknown host\n", 'red', True))

def getbyhostdns(host, port=None):
	#if ':' in #scan host:port -d
	pass