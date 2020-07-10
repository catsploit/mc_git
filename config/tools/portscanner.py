#!/usr/bin/python3
#-*- coding:utf-8 -*-

class Scannertool():
	def __init__(self, parameters):
		# - Declaring global variables for methods- #
		self.parameters = parameters #Flags while scanning the target, Ex: portscanner 0.0.0 -sV -O
		self.result = None
		self.target = None
		self.y = None
		self.server_banner = None
		self.server_jar = None
		self.server_users = None
		self.service = ""
		self.port_info_table = ""


	def scanning(self):
		import nmap
		from config.functions import sep_nmap_states, get_nmap_flags, cprint
		from config.colors import cyan, bold, red, green, yellow
		scanner = nmap.PortScanner()

		flags = self.parameters
		try:
			self.target = flags[0]
			port_range = flags[1]
			x = flags[2:]
			arguments = get_nmap_flags(x)

		except IndexError:
			return(cprint("[!] portscanner >> Invalid input\n", 'red', True))

		cprint("[~] portscanner > scanning . . . please wait\n", 'green', True)
		self.result = scanner.scan(self.target, port_range, arguments)
		#print(self.result) #test line, checking if something went wrong

		chain = ""
		table = """\
PORT   STATUS          SERVICE
----   ------          -------
{}
\
"""
		try:
			port_dictionary = self.result['scan'][self.target]['tcp']

		except Exception as e:
			return(cprint(f"[!] portscanner >> Error while parsing '{e}'\n", 'red', True))

		for i in port_dictionary:
			port_state = self.result['scan'][self.target]['tcp'][i]['state']
			str_state = sep_nmap_states(port_state)

			self.service = self.result['scan'][self.target]['tcp'][i]['name']
			i_format = f"{red}{bold}{i}   {str_state}"

			string = "{0:<15} {1:>19}\n".format(i_format, self.service)
			chain += string

			# - Personal flags for special tasks - #
			if '!minecraft_deep_scan' in x:
				self.y = i
				port_table = self.checking_minecraft_service()
				print(self.port_info_table.format(yellow + bold, bold, green,
					self.server_banner, self.server_jar, self.server_users, self.y))

		print('\n' + table.format(chain) + '\n')


	def checking_minecraft_service(self):
		# - 'minecraft' port service, showing JAR version, banner & users connected - #
		if self.service == 'minecraft':
			self.server_jar = self.result['scan'][self.target]['tcp'][self.y]['version'].replace('', 'null')
			self.server_info = self.result['scan'][self.target]['tcp'][self.y]['extrainfo'].replace('', 'null')

			if self.server_info != 'null':
				banner_in = server_info.index('Message')
				banner_end = server_info.index('User')

			else:
				banner_in = 0
				banner_end = 0 #XDDDD

			self.server_users = self.server_info[banner_end:]
			self.server_banner = self.server_info[banner_in:banner_end]

			self.port_info_table = """\
>> {6}{0}
x-----------------x
{2}{1}SERVER_BANNER:  {0}{3}
{2}{1}SERVER_JAR:	{0}{4}
{2}{1}SERVER_USERS:   {0}{5}
x-----------------x
\
"""
