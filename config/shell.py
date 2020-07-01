#!/usr/bin/python3
#_*_ coding:utf-8 _*_

import cmd
from config.functions import *
from config.colors import *
from config.tools.gethost import getbyhost


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
		get_args(args)
		if len(args) > 1:
			getbyhost(args)

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