#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('poet.db')
cursor = conn.cursor()
r = cursor.execute('select * from t_poetry where d_poetry LIKE "%%%s%%"' %'春眠不')
#print(r)
#print(len(list(r)))
#print(r)
#print(len(list(r)))
#print(r)
#print(len(list(r)))
if len(list(r))==1:
	for row in cursor:
		values1 = str(row[0]) 
	
	values_output1 = values1.replace("\\r\\n", " ")
	print(values_output1)
	

else:
	print('nothing')
cursor.close()
conn.close()