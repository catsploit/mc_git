#!/usr/bin/python3
# _*_ coding:utf8 _*_

import platform #temporary line deleting when using main file


def cprint(text='', color='', tbold=False, tsubline=False):
	global colors

	colors = {
	'bold': '\033[1m',
	'subline': '\033[4m',
	'red': '\033[0;31m',
	'cyan': '\033[0;36m',
	'green': '\033[0;32m'}

	selected_color = colors[color]
	using_bold = colors['bold']
	using_subline = colors['subline']

	if tbold & tsubline:
		print(f"{selected_color}{using_bold}{using_subline}{text}"); return 0

	elif tbold:
		print(f"{selected_color}{using_bold}{text}"); return 0

	elif tsubline:
		print(f"{selected_color}{using_subline}{text}"); return 0
	
	else:
		print(f"{selected_color}{text}"); return 0

def clear(os = platform.system()):
	if os != 'Linux':
		os.system('cls'); print('\n')

	else:
		os.system('clear'); print('\n')