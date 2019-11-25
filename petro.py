#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json

def ValorPetro():
	# Armado de request
	data = {'coins': ['PTR'], 'fiats': ['BS']}
	url = "https://petroapp-price.petro.gob.ve/price/"
	headers = {'Content-Type': 'application/json'}
	try:
		res = requests.post(url,data = json.dumps(data), headers = headers)
	except:
		return 0
	else:
		# Codigo http 200 = "success"
		if res.status_code == 200:
			res_json = res.json()
			return res_json['data']['PTR']['BS']
		else:
			return 0
