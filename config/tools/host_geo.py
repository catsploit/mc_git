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
	table = """\
	+--------------------------------------+
	|FIELD           |              CONTENT|
	+--------------------------------------+
	{}
	+--------------------------------------+\
	"""
	
	for i in info:
		extract = requesting(host)[i]
		print("{3}|{0:<15} >> {2}{1:>20}|".format(i, extract, white, cyan))
	print('\n')

#print("{0:<15} >> {2}{1:>20}".format(i, extract, white))