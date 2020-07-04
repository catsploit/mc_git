#!/usr/bin/python3
#-*- coding:utf-8 -*-

class Scannertool():
	def __init__(self, parameters):
		self.parameters = parameters #Flags while scanning the target, Ex: portscanner 0.0.0 -sV -v

	def scanning(self):
		import nmap
		from config.functions import sep_nmap_states, cprint
		from config.colors import cyan, bold, red
		scanner = nmap.PortScanner()

		flags = self.parameters
		try:
			target = flags[0]
			port_range = flags[1]
			x = flags[2:]; arguments = " ".join(x)

		except IndexError:
			return(cprint("[!] portscanner >> Invalid input\n", 'red', True))

		result = scanner.scan(target, port_range, arguments)

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

			string = "{0:<15} {1:>19}".format(i_format, service)
			chain += string

		print('\n' + table.format(chain) + '\n')


	def checking_minecraft_service(self):
		pass