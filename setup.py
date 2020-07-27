#!/usr/bin/python3
#-*- coding:utf-8 -*-
requirements = ['python-nmap']

from config.colors import *
from config.functions import cprint, clear
from sys import exit
from os import system

print(r"""{0}{1}
          _
         | |
 ___  ___| |_ _   _ _ __
/ __|/ _ \ __| | | | '_ \
\__ \  __/ |_| |_| | |_) |
|___/\___|\__|\__,_| .__/
                1.0| |
                   |_|{2}{3}[{1}mc_git.py{2}{3}]""".format(green, bold, normal, cyan) + '\n')

print("{0}{1}[-] >~ {2}Welcome to mc_git setup {0}{1}~< [-]".format(green, bold, white))
print("{1}{2}[{1}setup{2}] >> {3}Requirements to install >> {0}\n".format(requirements, cyan, bold, white))
install = input("[{0}{1}?{2}] {0}{1}Install? {2}y/n: ".format(black, bold, normal))
if install != 'y':
    exit(cprint("[!] Aborting . . .\n", 'red', True))
else:
    cprint("[setup] Installing  . . .\n", 'cyan', True)

# - Installing requirements - #
system("pip3 install -q python-nmap")

social_media = """
[{1}{0}GitHub{2}] catsploit
[{0}{3}Instagram{2}] @catsploit
[{0}{4}Telegram{2}] @catsploit\n""".format(bold, black, normal, magenta, cyan)
print(f'Support: {social_media}')

run = input("{0}{1}[+] {0}Set-up, run mc_git.py? y/n: {2}".format(green, bold, normal))
if run != 'y':
    exit(cprint("Bye!\n", 'cyan', True))

else:
    clear()
    system('python3 mc_git.py')
