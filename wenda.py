#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyrec
import wav2pcm
import baidu_ai
import play_mp3
import FAQ #问答

while True: 
	pyrec.rec("1.wav")

	pcm_file = wav2pcm.wav_to_pcm("1.wav")

	res_str = baidu_ai.audio_to_text(pcm_file)

	Q_str = FAQ.faq(res_str)

	synth_file = baidu_ai.text_to_audio(Q_str) 

	play_mp3.playmp3(synth_file)

	

