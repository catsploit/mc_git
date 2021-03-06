#!/usr/bin/python3
#_*_ coding:utf8 _*_

from config.functions import cprint, import_nmap
from config.shell import Shell
from sys import exit
import_nmap()

try:
	if __name__ == '__main__':
		shell_object = Shell()
		shell_object.cmdloop()

except KeyboardInterrupt:
	exit(cprint("[!] CTRL-C Interrupt, leaving . . .\n", 'red', True))
