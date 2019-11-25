#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
from petro import ValorPetro


def Insertar(precio):
	# Conecto para Consultar o Insertar
	db = pymysql.connect("localhost","admin","12345","Petro_Hist")
	cursor = db.cursor()

	# Preparo SQL query a INSERTAR
	sql = "INSERT INTO historico(moneda, precio) VALUES ('PTR', {0})".format(precio)
	
	try:
		# Execute the SQL
		cursor.execute(sql)
		db.commit()
		print("insertado valor en BD")
	except:
		# Rollback in case there is any error
		db.rollback()
		print("Error Insertando en BD")
				
	# desconectar del servidor
	db.close()


def Consultar():
	# Conecto para Consultar o Insertar
	db = pymysql.connect("localhost","admin","12345","Petro_Hist")
	cursor = db.cursor()
	# Preparo SQL query a CONSULTAR
	sql = "SELECT max(id), precio FROM historico GROUP by precio"
	
	# Execute the SQL
	cursor.execute(sql)
	results = cursor.fetchall()
	
	for row in results:
		max_valor = row[1]

	# desconectar del servidor
	db.close()

	return max_valor
		
		
