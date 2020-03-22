#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyaudio
import wave
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5


def rec(file_name):
	p = pyaudio.PyAudio()

	stream = p.open(format = FORMAT,
				channels = CHANNELS,
				rate=RATE,
				input = True,
				frames_per_buffer=CHUNK)

	print("开始录音, 请说话.......")

	frames = []

	for i in range(0, int(RATE/CHUNK *RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)

	print("录音结束，请不要出声！")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(file_name, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

