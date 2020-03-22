from aip import AipSpeech
APP_ID = "16447821"
API_KEY = "gy12LoIw322GrnvPWgcbMeBX"
SECRET_KEY = "iGcpEEbblpN9tvKukrrfTgxrNGejpk9g"

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def audio_to_text(pcm_file):
	with open(pcm_file,'rb') as fp:
		file_context = fp.read()

	res = client.asr(file_context, 'pcm', 16000, {
		'dev_pid': 1537,
	})


	if(len(res))!=3:
		res_str = res.get("result")[0].replace("。","")

		return res_str
	else:
		print("您没有说话啊")


	


def text_to_audio(res_str):
	synth_file = "synth.mp3"
	synth_context = client.synthesis(res_str,"zh", 1, {
	"vol":5,
	"spd":4,
	"pit":9,
	"per": 3
	})

	with open(synth_file, "wb") as f:
		f.write(synth_context)

	return synth_file
