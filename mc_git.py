#!/usr/bin/python3
#_*_ coding:utf8 _*_

#from config.functions import cprint
#from config.functions import clear
from config.shell import Shell

import socket
import os
import getpass
import requests
import json
import dns.resolver


if __name__ == '__main__':
	shell_object = Shell()
	shell_object.cmdloop()