#!/usr/bin/python3
#_*_ coding:utf8 _*_

import sys
import socket
import os
import getpass
import requests
import json
import dns.resolver

try:
	import nmap
except:
	sys.exit('\n[!] ImportError exception, please make sure that you have nmap\n')


def cprint(text='', color='', tbold=False, tsubline=False):
	global colors

	colors = {
	'bold': '\033[1m',
	'subline': '\033[4m',
	'red': '\033[0;31m',
	'cyan': '\033[0;36m',
	'green': '\033[0;32m'}

	for i in colors:
		if i == color:
			using_color = colors[color]
			if tbold:
				using_bold = colors['bold']
				print(f'{using_color}' + f'{using_bold}' + f'{text}')
				return 0

			else:
				print('using no bold format') #test line
				print(f'{using_color}' + f'{text}')
				return 0

cprint('texto de prueba para comprobar que esta mierda funciona', 'cyan')


