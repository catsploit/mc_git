#!/usr/bin/python3
# _*_ coding:utf-8 _*_

import platform
import sys
import getpass
from subprocess import call
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


def clear(os = platform.system()):
	if os != 'Linux':
		call('cls'); print('\n')

	else:
		call('clear'); print('\n')


def leave():
	sys.exit(cprint("[-] Leaving . . .\n", 'cyan', True))


def print_banner():
	user = getpass.getuser()
	banner = f'''
		 ███▄ ▄███░ ▄████▄       ▄████  ██░▄▄▄█████░
		░██░▀█▀ ██░░██▀ ▀█      ██░ ▀█░░██░░  ██░ ░░
		░██    ░██░░▓█    ▄    ░██░▄▄▄░░██░░ ░██░ ░░ 
		░██    ░██ ░▓▓▄ ▄██░   ░▓█  ██░░██░░ ░██░ ░ 
		░██░   ░██░░ ▓███▀ ░   ░░▓███▀░░██░  ░██░ ░ [1.0]
		░ ░░   ░  ░░ ░░ ░  ░    ░░   ░ ░░    ░ ░░
		░  ░      ░  ░  ░        ░   ░  ░ ░    ░    {cyan}Hi! {bold}{user}{normal}
		░      ░   ░           ░ ░   ░  ░ ░  ░      
    	   		░   ░ ░               ░  ░           
           		░                                 \n'''.replace('░', f'{red}░{white}')
	
	return banner


def get_args(parameters):
	if len(parameters) > 1:
		arguments = parameters.split(' ')
		#print(arguments)
		return arguments

	else:
		return(cprint("[!] Missing arguments\n", 'red', True))