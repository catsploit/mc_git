#!/usr/bin/python3
#_*_ coding:utf-8 _*_

import socket
import dns.resolver
from config.functions import cprint
from config.colors import *

def getbyhost(host):
	try:
		hostIP = socket.gethostbyname(host)
		return(print("{2}{3}[-]{2} Done! {3}{0}{2} >> {3}{1}\n".format(host, hostIP, cyan, bold)))

	except socket.gaierror:
		return(cprint("[!] gethost >> Unknown host\n", 'red', True))


def getbyhostdns(hostscan):
	host = hostscan
	port=None

	if ':' in host:
		entry = host.split(':')

		host = str(entry[0])
		port = int(entry[1])

	if not port:
		port = 25565
		try:
			request = dns.resolver.query(f'_minecraft._tcp.{host}', 'SRV')
			if len(request):
				get_request = request[0]
				host = str(get_request.target).rstrip('.')
				port = int(get_request.port)

		except dns.resolver.NXDOMAIN:
			return(cprint("[!] gethost >> DNS query doesn't exist\n", 'red', True))

	return(print("{2}{3}[-] {2}Done! {3}'{0}'{2} >> {3}{1}\n".format(hostscan, socket.gethostbyname(host), cyan, bold)))
