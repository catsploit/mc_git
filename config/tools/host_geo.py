#!/usr/bin/python3
#-*- coding:utf-8 -*-

from requests import get
from config.colors import *
from config.functions import cprint
import json


def geolocate_host(host):
	host = host
	api = f'http://ip-api.com/json/{host}'
	info = 'status,country,regionName,city,zip,lat,lon,isp,as,org'
	data = {'fields': info}

	def requesting(host):
		request = get(api, data=data)
		json_request = json.loads(request.content)
		return json_request

	info = info.split(',')
	table = """{}\

+--------------------------------------+
|FIELD           |              CONTENT|
|--------------------------------------|
{}+--------------------------------------+\
"""

	try:
		chain = ""
		for i in info:
			extract = requesting(host)[i]
			text = "|{3}{0:<15}{2} >> {4}{3}{1:>19}{2}|\n".format(i, extract, cyan, bold, green)
			chain += text

		formatted_table = table.format(cyan, chain) + '\n'
		return(formatted_table)

	except KeyError:
		cprint("[!] geolocate >> Unknown address\n", 'red', True)
