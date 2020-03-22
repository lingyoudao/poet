#!/usr/bin/python 
# -*- coding: utf-8 -*-
import sqlite3
def poetmatch(str1): 
	conn = sqlite3.connect('poet.db')
	cursor = conn.cursor()
	c1 = cursor.execute('select * from t_poetry where d_poetry LIKE "%%%s%%"' %str1)

	if c1.fetchall() != []:

		print('找到啦!')
		c2 = cursor.execute('select * from t_poetry where d_poetry LIKE "%%%s%%"' %str1)
		for row in c2:
			values = str(row[0])
		values_output1 = values.replace("\\r\\n", " ").replace('[1]',' ').replace('[2]',' ').replace('[3]',' ').replace('[4]',' ').replace('[5]',' ').replace('\'',' ')
#使用str转化list，再使用replace方法
		print(values_output1)
		return values_output1
	else:
		print('对不起，没找到，要不重新试一遍？或者换一首？')
		return 0
	
	cursor.close()
	conn.close()