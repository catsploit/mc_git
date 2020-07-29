#!/usr/bin/python3
# _*_ coding:utf-8 _*_

from platform import system
from sys import exit
from subprocess import call
from getpass import getuser
from config.colors import *


def cprint(text='', color='', tbold=False, tsubline=False, ending='\n'):
	colors = {
	'bold': '\033[1m',
	'subline': '\033[4m',
	'red': '\033[0;31m',
	'cyan': '\033[0;36m',
	'green': '\033[0;32m',
	'yellow': '\033[0;33m',
	'white': '\033[0;37m'}

	selected_color = colors[color]
	using_bold = colors['bold']
	using_subline = colors['subline']

	if tbold & tsubline:
		print(f"{selected_color}{using_bold}{using_subline}{text}", end=ending); return 0

	elif tbold:
		print(f"{selected_color}{using_bold}{text}", end=ending); return 0

	elif tsubline:
		print(f"{selected_color}{using_subline}{text}", end=ending); return 0

	else:
		print(f"{selected_color}{text}", end=ending); return 0


def clear(os = system()):
	if os != 'Linux':
		call('cls'); print('\n')

	else:
		call('clear'); print('\n')


def leave():
	exit(cprint("[-] Leaving . . .\n", 'cyan', True))


def print_banner():
	banner = f'''
		 ███▄ ▄███░ ▄████▄       ▄████  ██░▄▄▄█████░
		░██░▀█▀ ██░░██▀ ▀█      ██░ ▀█░░██░░  ██░ ░░
		░██    ░██░░▓█    ▄    ░██░▄▄▄░░██░░ ░██░ ░░
		░██    ░██ ░▓▓▄ ▄██░   ░▓█  ██░░██░░ ░██░ ░    ({red}Project log 1.0{white})
		░██░   ░██░░ ▓███▀ ░   ░░▓███▀░░██░  ░██░ ░    {red}{bold}[-]{white} File output option (Cancelled)
		░ ░░   ░  ░░ ░░ ░  ░    ░░   ░ ░░    ░ ░░      {green}{bold}[+]{white} Instead, added output file with server info
		░  ░      ░  ░  ░        ░   ░  ░ ░    ░
		░      ░   ░           ░ ░   ░  ░ ░  ░
    	   		░   ░ ░               ░  ░
           		░                                 \n'''.replace('░', f'{red}░{white}')

	return banner


def get_args(parameters):
	if len(parameters) > 1:
		arguments = parameters.split(' ')
		return arguments

	else:
		return(cprint("[!] Missing arguments\n", 'red', True))


def import_nmap():
	try:
		import nmap
	except ImportError:
		sys.exit(cprint("[!] portscanner >> ImportError exception, fix it by installing nmap\n", 'red', True))


def sep_nmap_states(port_state):
	states = {'open': green, 'filtered': cyan, 'closed': red}

	for i in states:
		if port_state == i:
			return(f'{states[i]}{bold}{i}')

def is_root(user = getuser()):
	if user != "root":
		return False
	return True
