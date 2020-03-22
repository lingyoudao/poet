#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
from time import sleep
import os
def playmp3(file_name):
	os.system(os.getcwd()+"\\"+"ffplay -autoexit %s" %(file_name))
	num = os.getpid()
	os.system("taskkill /pid "+str(num)+" /f")

if __name__ == "__main__":
		print ("父进程启动")
		p = Process(target=playmp3("synth.mp3"))
		p.start()
		p.join()
				
		print ("父进程结束")