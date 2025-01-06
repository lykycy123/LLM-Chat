
import torchaudio
from funasr import AutoModel
from IPython.display import Audio

speaker1_wav = r'.\output\audio_6.wav'
waveform, sample_rate = torchaudio.load(speaker1_wav)
Audio(waveform, rate=sample_rate, autoplay=True)

# VAD检测
from funasr import AutoModel
model = AutoModel(model="paraformer-zh")
res = model.generate(input=speaker1_wav)

prompt = res[0]['text'].split(">")[-1]

print(res)
print("user:",prompt)



# # 多说话人语音识别
# funasr_model = AutoModel(model="iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
#                         vad_model="damo/speech_fsmn_vad_zh-cn-16k-common-pytorch",
#                         punc_model="damo/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
#                         spk_model="damo/speech_campplus_sv_zh-cn_16k-common",
#                         )
# res = funasr_model.generate(input=f"multi_speaker.wav", 
#             batch_size_s=300)
# print(res[0]['text'])
# res_srt = generate_srt(res[0]['sentence_info'])
# print(res_srt)

