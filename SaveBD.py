#!/usr/bin/python3
# -*- coding: utf-8 -*-

from BD import Insertar, Consultar
from petro import ValorPetro

# Consulto valor PTR en API
precio = ValorPetro()
ult_valor = Consultar()

# Inserto el Valor en BD si el precio !=0
if precio:
	if precio != ult_valor:
		Insertar(precio)
	else:
		print("Ya esta actualizado!")
else:
	print("Error obteniendo valor de PTR")
	
Consultar()
