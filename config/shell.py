#!/usr/bin/python3
#_*_ coding:utf-8 _*_

import cmd
from config.functions import *
from config.colors import *
from config.tools.gethost import getbyhost, getbyhostdns
from config.tools.host_geo import geolocate_host
from config.tools.portscanner import Scannertool


class Shell(cmd.Cmd):
	user = getpass.getuser()
	prompt = "{0}{1}{2}~/{1}mcgit@{3}${4}{5} ".format(green, bold, subline, user, normal, white)

	def do_test(self, args):
		print("This is a test line XD\n")

	def do_clear(self, args):
		clear()

	def do_help(self, args):
		cprint("actually there is nothing to see here...\n", "green")

	def do_exit(self, args):
		leave()

	def do_gethost(self, args):
		flags = get_args(args)
		
		if flags != 0:
			if len(flags) == 1:
				getbyhost(flags[0])
			elif len(flags) == 2 and flags[1] == '-d':
				getbyhostdns(flags[0])
			else:
				cprint("[!] gethost >> Invalid input\n", 'red', True)

	def do_geolocate(self, args):
		flags = get_args(args)
		if flags != 0:
			if len(flags) == 1:
				geolocate_host(flags[0])
			else:
				cprint("[!] geolocate >> Invalid input\n", 'red', True)

	def do_portscanner(self, args):
		import_nmap()
		flags = get_args(args)

		if flags != 0:
			scanning_tool = Scannertool(flags)
			scanning_tool.scanning()

	def emptyline(self):
		pass

	def default(self, args):
		cprint(f"[!] cmd >> Unknown command '{args}'\n", 'red', True)

	def preloop(self):
		clear()
		print(print_banner())