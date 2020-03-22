#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
def playmp3(file_name):
	os.system(os.getcwd()+"\\"+"ffplay -autoexit %s" %(file_name))
	
