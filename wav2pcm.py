#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
def wav_to_pcm(wav_file):
	pcm_file = "%s.pcm" %(wav_file.split(".")[0])
	print(os.getcwd()+"\\"+"ffmpeg.exe")
	os.system(os.getcwd()+"\\"+"ffmpeg -y -i %s -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s" %(wav_file, pcm_file))
	return pcm_file
