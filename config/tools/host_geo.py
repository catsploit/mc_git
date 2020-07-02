#!/usr/bin/python3
#-*- coding:utf-8 -*-

import requests
import json
from config.colors import *
from config.functions import cprint


def geolocate_host(host):
	host = host
	api = f'http://ip-api.com/json/{host}'
	info = 'status,country,regionName,city,zip,lat,lon,isp,as,org'
	data = {'fields': info}

	def requesting(host):
		request = requests.get(api, data=data)
		json_request = json.loads(request.content)
		return json_request

	info = info.split(',')
	table = """{}\

+--------------------------------------+
|FIELD           |              CONTENT|
|--------------------------------------|
{}+--------------------------------------+\
"""

	#print(table, end='')
	try:
		chain = ""
		for i in info:
			extract = requesting(host)[i]
			text = "|{3}{0:<15}{2} >> {4}{3}{1:>19}{2}|\n".format(i, extract, cyan, bold, green)
			chain += text

		print(table.format(cyan, chain) + '\n')
	except KeyError:
		cprint("[!] geolocate >> Unknown address\n", 'red', True)