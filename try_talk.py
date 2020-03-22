#!/usr/bin/python
# -*- coding: utf-8 -*-
from aip import AipSpeech
APP_ID = "16447821"
API_KEY = "gy12LoIw322GrnvPWgcbMeBX"
SECRET_KEY = "iGcpEEbblpN9tvKukrrfTgxrNGejpk9g"

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
res = client.synthesis('春眠不觉晓处处闻啼鸟夜来风雨声花落知多少', 'zh', 1)
print(res)
with open("s1.mp3", "wb") as f:
	f.write(res)