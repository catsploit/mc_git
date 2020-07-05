#!/usr/bin/python3
#-*- coding:utf-8 -*-

class Scannertool():
	def __init__(self, parameters):
		self.parameters = parameters #Flags while scanning the target, Ex: portscanner 0.0.0 -sV -v
		self.results = []
		self.service = ''


	def scanning(self):
		import nmap
		from config.functions import sep_nmap_states, get_nmap_flags, cprint
		from config.colors import cyan, bold, red, green
		scanner = nmap.PortScanner()

		results = self.results
		service = self.service
		flags = self.parameters
		try:
			target = flags[0]
			port_range = flags[1]
			x = flags[2:]#; arguments = " ".join(x)
			arguments = get_nmap_flags(x)
			#print(x)

		except IndexError:
			return(cprint("[!] portscanner >> Invalid input\n", 'red', True))

		result = scanner.scan(target, port_range, arguments)
		print(result) #test line, checking if something went wrong

		chain = ""
		table = """\
PORT   STATUS          SERVICE
----   ------          -------
{}		
\
"""
		try:
			port_dictionary = result['scan'][target]['tcp']

		except Exception as e:
			return(cprint(f"[!] portscanner >> Error while parsing '{e}'\n", 'red', True))

		for i in port_dictionary:
			port_state = result['scan'][target]['tcp'][i]['state']
			str_state = sep_nmap_states(port_state)

			service = result['scan'][target]['tcp'][i]['name']
			i_format = f"{red}{bold}{i}   {str_state}"

			string = "{0:<15} {1:>19}\n".format(i_format, service)
			chain += string

			# - Personal flags for special tasks - #
			if '!minecraft_deep_scan' in x:
				port_table = self.checking_minecraft_service()
				print(port_table)
				#print(port_info_table.format(cyan, bold, green, server_banner, server_jar, server_users, i))

		print('\n' + table.format(chain) + '\n')


	def checking_minecraft_service(self):
		# - 'minecraft' port service, showing JAR version, banner & users connected - #
		#print(self.service)
		if self.service == 'minecraft':
			server_jar = result['scan'][target]['tcp'][i]['version']
			server_info = result['scan'][target]['tcp'][i]['extrainfo']

			banner_in = server_info.index('Message')
			banner_end = server_info.index('User')
			server_users = server_info[banner_end:]
			server_banner = server_info[banner_in:banner_end]

			port_info_table = """\
			>> {6}{0}
			x-----------------x
			{2}{1}SERVER_BANNER:{0}{3}
			{2}{1}SERVER_JAR:	{0}{4}
			{2}{1}SERVER_USERS: {0}{5}
			x-----------------x
			\
			"""
			return(print(port_info_table.format(cyan, bold, green, server_banner, server_jar, server_users, i)))