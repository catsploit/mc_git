#!/usr/bin/python3
#_*_ coding:utf8 _*_

#from config.functions import clear
from config.functions import cprint
from config.shell import Shell
import sys
try:
	import nmap
except ImportError:
	sys.exit(cprint('[!] ImportError exception\n', 'red'))


if __name__ == '__main__':
	shell_object = Shell()
	shell_object.cmdloop()