#!/usr/bin/python3
#_*_ coding:utf8 _*_

import cmd
from config.functions import cprint
from config.functions import clear
from config.functions import leave
from config.functions import print_banner
from config.functions import welcome

class Shell(cmd.Cmd):
	bold = '\033[1m'
	subline = '\033[4m'
	normal = '\033[0m'
	red = '\033[0;31m'
	cyan = '\033[0;36m'
	green = '\033[0;32m'
	white = '\033[0;37m'

	prompt = f"{green}{bold}{subline}~/mcgit${normal}{white} "

	def do_test(self, args):
		print("This is a test line XD\n")

	def do_clear(self, args):
		clear()

	def do_help(self, args):
		cprint("actually there is nothing to see here...\n", "green")

	def do_exit(self, args):
		leave()

	def emptyline(self):
		pass

	def default(self, args):
		cprint(f"[!] Unknown command '{args}'\n", 'red', True)

	def precmd(self, args):
		args = args.lower()
		return(args)

	def preloop(self):
		clear()
		print_banner()