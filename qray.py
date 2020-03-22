#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyrec
import wav2pcm
import baidu_ai
import play_mp3
#import FAQ
import opendb

while 1:

	pyrec.rec("1.wav")

	pcm_file = wav2pcm.wav_to_pcm("1.wav")
	print(pcm_file)

	res_str = baidu_ai.audio_to_text(pcm_file)

	print(res_str)

	#Q_str = FAQ.faq(res_str)

	Q_str = opendb.poetmatch(res_str)
	
	
	if Q_str != 0: 

		synth_file = baidu_ai.text_to_audio(Q_str)


	#synth_file = baidu_ai.text_to_audio(res_str) 


		play_mp3.playmp3(synth_file)

	else:
		continue

	