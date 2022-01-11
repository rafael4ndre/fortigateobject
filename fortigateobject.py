#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Rafael Andre de Oliveira (NuxMorpheus)  
# Creation Date: 11/01/2022
# version ='1.0'
# ---------------------------------------------------------------------------
# This module generate a script to create Fortigate firewall address 
# objects, reading the IP adresses from a txt file. 
# ---------------------------------------------------------------------------

import sys

length = len(sys.argv)


if length<2:
	print("######")
	print("Please, pass the IP file as an agurment:")
	print("USAGE: fortigateobject.py <IP file>")
	print("######")
else:
	with open(sys.argv[1]) as myfile:
		count=0
		print("config firewall address")
		for line in myfile:
			name="block_"+line
			print("edit", name, sep=' ', end='')
			object=line.rstrip("\n")
			print("set subnet", object, "255.255.255.255", sep=' ')
			print("next")
			count=count+1
	myfile.close()
	print ("end")
