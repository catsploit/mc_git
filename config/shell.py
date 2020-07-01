#!/usr/bin/python3
#_*_ coding:utf-8 _*_

import cmd
from config.functions import *
from config.colors import *
from config.tools.gethost import getbyhost, getbyhostdns
from config.tools.host_geo import geolocate_host


class Shell(cmd.Cmd):
	prompt = f"{green}{bold}{subline}~/mcgit${normal}{white} "

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
			#print(flags)
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

	def emptyline(self):
		pass

	def default(self, args):
		cprint(f"[!] Unknown command '{args}'\n", 'red', True)

	def precmd(self, args):
		args = args.lower()
		return(args)

	def preloop(self):
		clear()
		print(print_banner())