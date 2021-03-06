#!/usr/bin/python3
#_*_ coding:utf-8 _*_

import cmd
from config.functions import *
from config.colors import *
from config.tools.gethost import getbyhost, getbyhostdns
from config.tools.getenv import getEnvironment
from config.tools.host_geo import geolocate_host
from config.tools.osmatch import os_match
from config.tools.portscannertool import Scannertool


class Shell(cmd.Cmd):
	user = getuser()
	prompt = "{0}{1}{2}~/{1}mcgit@{3}${4}{5} ".format(green, bold, subline, user, normal, white)

	def do_test(self, args):
		print("This is a test line XD\n")

	def do_clear(self, args):
		clear()

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
				print(geolocate_host(flags[0]))
			else:
				cprint("[!] geolocate >> Invalid input\n", 'red', True)

	def do_portscanner(self, args):
		import_nmap()
		flags = get_args(args)
		if flags != 0:
			try:
				target = flags[0]
				port_range = flags[1]
				parameters = flags[2:]
			except IndexError as e:
				cprint(f"[!] portscanner >> Invalid input: {e}\n", 'red', True)
			else:
				Scannertool(target, port_range, parameters).port_lookup()

	def do_getenv(self, args):
		import_nmap()
		parameters = get_args(args)
		if parameters != 0:
				getEnvironment(parameters)

	def do_osmatch(self, args):
		parameters = get_args(args)
		if parameters != 0:
			target = parameters[0]
			os_match(target, True)

	def do_help(self, args):
		print("\nI=================================================================================================I")
		print("|Showing help list:                                                                               |")
		print("|gethost <hostname> <[-d]>                :get hostname's ip, can specify a dns query by using -d |")
		print("|geolocate <ip>                           :geolocate an ip by using the ip-api                    |")
		print("|portscanner <ip> <port_range> <flags>    :scan server's ports, returning information about it    |")
		print("|getenv <host>                            :get host's environment (OS, Jar, Ubication, etc)       |")
		print("|clear                                    :if your terminal is messed up                          |")
		print("|exit                                     :leave the program                                      |")
		print("I=================================================================================================I\n")

	def emptyline(self):
		pass

	def default(self, args):
		cprint(f"[!] cmd >> Unknown command '{args}'\n", 'red', True)

	def preloop(self):
		clear()
		print(print_banner())
